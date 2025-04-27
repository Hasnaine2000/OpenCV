import cv2
import numpy as np

# Load an image
image = cv2.imread('example.jpg')  # Replace 'example.jpg' with your image path

# Define a sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# Apply the kernel to the image
sharpened = cv2.filter2D(image, -1, kernel)

cv2.imshow('Original', image)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()