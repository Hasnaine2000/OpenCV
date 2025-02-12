import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#Haar cascade is a pretained classifier that can detect faces and frontal face is the specific classifier that we want

face_cascade = cv2.CascadeClassifier(cv2.data.harcascades + 'haarcascade_frontalface_default.xml' )
eye_cascade = cv2.CascadeClassifier(cv2.data.harcascades + 'haarcascade_frontalface_default.xml' )


while True:
    ret,frame = cap.read()  
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):  
        break 
    
cap.release()
cv2.destroyAllWindows()