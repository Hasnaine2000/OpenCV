import cv2

# Load an image in grayscale
image = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)  # Replace 'example.jpg' with your image path

# Apply histogram equalization
equalized = cv2.equalizeHist(image)

cv2.imshow('Original', image)
cv2.imshow('Equalized', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()