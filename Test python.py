import face_recognition
import cv2
import numpy as np

import cv2
import face_recognition

def load_and_encode(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Error: Could not load image from {image_path}. Check the file path and format.")

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
    encoding = face_recognition.face_encodings(rgb_image)

    return encoding[0] if encoding else None  



one_encoding = load_and_encode("Photos/one.jpg")
two_encoding = load_and_encode("Photos/two.jpg")
three_encoding = load_and_encode("Photos/three.jpg")
four_encoding = load_and_encode("Photos/four.jpg")

known_face_encoding = [one_encoding, two_encoding, three_encoding, four_encoding]
known_face_names = ["one", "two", "three", "four"]

students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s= True

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()  #frame = numpy array that is going to represesnt the image and ret = is it working properly
    small_frame = cv2.resize(frame,(0,0),0.25,0.25)
    
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces (known_face_encoding,face_encoding)
            name = " "
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
    
    
    
    if cv2.waitKey(1) == ord('q'):  #button to close the webcam
      break 
    
    
cap.release()
cv2.destroyAllWindows()
