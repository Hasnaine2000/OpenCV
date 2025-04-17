import cv2

# Load an image
image = cv2.imread('example.jpg')  # Replace 'example.jpg' with your image path

# Create image pyramid
smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(image)

cv2.imshow('Original', image)
cv2.imshow('Smaller', smaller)
cv2.imshow('Larger', larger)
cv2.waitKey(0)
cv2.destroyAllWindows()