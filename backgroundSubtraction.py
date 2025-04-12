import cv2

cap = cv2.VideoCapture('video.mp4')  # Replace 'video.mp4' with your video path
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    fgmask = fgbg.apply(frame)

    cv2.imshow('Original', frame)
    cv2.imshow('Foreground Mask', fgmask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()