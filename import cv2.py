import cv2

# Load an image
image = cv2.imread('example.jpg')  # Replace 'example.jpg' with your image path

# Flip the image
flipped_horizontally = cv2.flip(image, 1)  # Horizontal flip
flipped_vertically = cv2.flip(image, 0)   # Vertical flip
flipped_both = cv2.flip(image, -1)        # Both horizontal and vertical flip

cv2.imshow('Original', image)
cv2.imshow('Flipped Horizontally', flipped_horizontally)
cv2.imshow('Flipped Vertically', flipped_vertically)
cv2.imshow('Flipped Both', flipped_both)
cv2.waitKey(0)
cv2.destroyAllWindows()