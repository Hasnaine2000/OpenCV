import cv2

# Load the main image and the template
image = cv2.imread('example.jpg')  # Replace 'example.jpg' with your image path
template = cv2.imread('template.jpg')  # Replace 'template.jpg' with your template path

# Perform template matching
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Draw a rectangle around the matched region
top_left = max_loc
h, w = template.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

cv2.imshow('Matched Template', image)
cv2.waitKey(0)
cv2.destroyAllWindows()