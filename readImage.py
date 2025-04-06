import cv2

# Read an image from a file
image = cv2.imread('path_to_your_image.jpg')

# Display the image in a window
cv2.imshow('Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()