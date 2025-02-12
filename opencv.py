import cv2

img = cv2.imread('randomdog.jpg', -1)
if img is None:
    print("Error: Image not found.")



cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#  second argument of imread = -1 transparency would be ignored 0 load in grascale mode 1 as it is 