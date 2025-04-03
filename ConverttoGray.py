import cv2

# Load an image
image = cv2.imread('example.jpg')  # Replace 'example.jpg' with your image path

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()