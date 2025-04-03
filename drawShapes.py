import cv2
import numpy as np

# Create a blank white image
image = np.ones((400, 400, 3), dtype=np.uint8) * 255

# Draw a blue line
cv2.line(image, (50, 50), (350, 50), (255, 0, 0), 5)

# Draw a green rectangle
cv2.rectangle(image, (50, 100), (350, 300), (0, 255, 0), -1)

# Draw a red circle
cv2.circle(image, (200, 350), 50, (0, 0, 255), -1)

# Display the image with shapes
cv2.imshow('Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()