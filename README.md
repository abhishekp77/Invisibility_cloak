# Invisibility_cloak
This project is a simple implementation of the invisibility cloak effect using OpenCV. The idea is inspired by the popular concept of disappearing objects, where a specific colored cloak becomes invisible by replacing it with the background. The project is built using basic image processing techniques such as color detection, masking, and background subtraction.

**How It Works**

The system first captures the static background for a few seconds when no person is in the frame. This background is later used to replace the cloak region.

The input frame from the webcam is converted from BGR to HSV color space. HSV makes it easier to detect specific colors compared to RGB.

Trackbars are provided so the user can adjust the lower and upper HSV ranges in real time. These ranges define the cloak’s color (blue in this case).

A binary mask is created for the selected color region, highlighting the cloak area in white.

Morphological operations such as opening and dilation are applied to the mask to remove noise and improve smoothness.

The mask is inverted to separate cloak and non-cloak regions.

Pixels from the cloak area are replaced with the background, while the remaining pixels show the original frame.

The final blended output creates the illusion that the cloak is invisible.

**Requirements**

Python 3.x

OpenCV

Numpy

**Install the required libraries using:**

pip install opencv-python numpy

**Usage**

Clone the repository and navigate to the project directory.

**Run the script using:**

python cloak.py


Step out of the camera frame for three seconds to allow the system to capture the background.

Wear or hold a cloak of solid blue color in front of the camera.

Adjust the trackbars for lower and upper HSV values until the cloak area is correctly detected.

Press q to quit the program.

**Trackbar Controls**

LH, LS, LV represent the lower hue, saturation, and value.

UH, US, UV represent the upper hue, saturation, and value.

Proper adjustment ensures accurate color detection for the cloak.

**Limitations**

Works only with solid, bright-colored cloaks (preferably blue, red, or green).

Sensitive to lighting conditions and shadows, which may affect color detection.

Requires the background to remain static while running.

Some flickering may occur around cloak edges due to imperfect masking.

**Future Enhancements**

Integration of AI-based human segmentation models (MediaPipe, DeepLab, or similar) for more reliable detection.

Improved smoothing techniques to reduce flickering at cloak boundaries.

Support for detecting and processing multiple cloak colors automatically.

Dynamic background handling for better realism.
