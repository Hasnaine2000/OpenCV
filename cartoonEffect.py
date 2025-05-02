import cv2
import numpy as np

# Load an image
image = cv2.imread('example.jpg')  # Replace 'example.jpg' with your image path

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply median blur
gray = cv2.medianBlur(gray, 5)

# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# Apply bilateral filter to smooth the image
color = cv2.bilateralFilter(image, 9, 300, 300)

# Combine edges and smoothed image
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow('Original', image)
cv2.imshow('Cartoon Effect', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()