import cv2
import numpy as np

# Load an image
image = cv2.imread('example.jpg')  # Replace 'example.jpg' with your image path

# Define the translation matrix
rows, cols = image.shape[:2]
M = np.float32([[1, 0, 100], [0, 1, 50]])  # Shift 100 pixels right and 50 pixels down

# Apply the translation
translated = cv2.warpAffine(image, M, (cols, rows))

cv2.imshow('Original', image)
cv2.imshow('Translated', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()