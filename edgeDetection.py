import cv2

# Load an image in grayscale
image = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)  # Replace 'example.jpg' with your image path

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()