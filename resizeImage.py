import cv2

# Load an image
image = cv2.imread('example.jpg')  # Replace 'example.jpg' with your image path

# Resize the image
resized = cv2.resize(image, (300, 300))

cv2.imshow('Original', image)
cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()