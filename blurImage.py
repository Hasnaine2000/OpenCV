import cv2

# Load an image
image = cv2.imread('example.jpg')  # Replace 'example.jpg' with your image path

# Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imshow('Original', image)
cv2.imshow('Blurred', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()