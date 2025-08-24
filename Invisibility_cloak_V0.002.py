import cv2
import mediapipe as mp
import numpy as np
import time

# Initialize MediaPipe Selfie Segmentation
mp_selfie_segmentation = mp.solutions.selfie_segmentation
segment = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

cap = cv2.VideoCapture(0)

# Capture background
time.sleep(2)
for i in range(30):
    ret, background = cap.read()
background = cv2.flip(background, 1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Step 1: Human segmentation
    results = segment.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    human_mask = results.segmentation_mask > 0.5
    human_mask = human_mask.astype(np.uint8) * 255

    # Step 2: Cloak (blue color detection)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 80, 40])   # adjust for your cloak shade
    upper_blue = np.array([130, 255, 255])
    cloak_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Step 3: Combine cloak mask with human mask
    final_mask = cv2.bitwise_and(cloak_mask, human_mask)

    # Step 4: Apply mask → replace cloak area with background
    cloak_area = cv2.bitwise_and(background, background, mask=final_mask)
    rest_area = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(final_mask))
    output = cv2.addWeighted(cloak_area, 1, rest_area, 1, 0)

    cv2.imshow("AI Cloak", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
