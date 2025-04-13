import cv2

# Load an image
image = cv2.imread('example.jpg')  # Replace 'example.jpg' with your image path

# Convert to different color spaces
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imshow('Original', image)
cv2.imshow('Grayscale', gray)
cv2.imshow('HSV', hsv)
cv2.imshow('LAB', lab)
cv2.waitKey(0)
cv2.destroyAllWindows()