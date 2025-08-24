import cv2
import time
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
time.sleep(3)

for i in range(30):
    ret, background = cap.read()
background = cv2.flip(background, 1)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("LH", "Trackbars", 90, 180, nothing)  # Lower Hue
cv2.createTrackbar("LS", "Trackbars", 80, 255, nothing)  # Lower Saturation
cv2.createTrackbar("LV", "Trackbars", 40, 255, nothing)  # Lower Value
cv2.createTrackbar("UH", "Trackbars", 130, 180, nothing) # Upper Hue
cv2.createTrackbar("US", "Trackbars", 255, 255, nothing) # Upper Saturation
cv2.createTrackbar("UV", "Trackbars", 255, 255, nothing) # Upper Value

print("Background captured")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    l_h = cv2.getTrackbarPos("LH", "Trackbars")
    l_s = cv2.getTrackbarPos("LS", "Trackbars")
    l_v = cv2.getTrackbarPos("LV", "Trackbars")
    u_h = cv2.getTrackbarPos("UH", "Trackbars")
    u_s = cv2.getTrackbarPos("US", "Trackbars")
    u_v = cv2.getTrackbarPos("UV", "Trackbars")

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=1)

    inv_mask = cv2.bitwise_not(mask)

    res1 = cv2.bitwise_and(frame, frame, mask=inv_mask)
    res2 = cv2.bitwise_and(background, background, mask=mask)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisibility Cloak", final_output)
    cv2.imshow("Mask", mask)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
