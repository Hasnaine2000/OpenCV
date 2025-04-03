import cv2

# Read an image from a file
image = cv2.imread('path_to_your_image.jpg')

# Check if the image was successfully loaded
if image is not None:
    # Write the image to a new file
    cv2.imwrite('output_image.jpg', image)
else:
    print("Error: Could not read the image.")