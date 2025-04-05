import cv2
import numpy as np

# Read the image
image = cv2.imread('path_to_your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply binary thresholding
_, binary_threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Apply adaptive thresholding
adaptive_threshold = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                           cv2.THRESH_BINARY, 11, 2)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Binary Threshold', binary_threshold)
cv2.imshow('Adaptive Threshold', adaptive_threshold)

# Wait until a key is pressed and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()