import face_recognition
import cv2
import numpy as np

one_image = face_recognition.load_image_file("Photos/one.jpg")
one_encoding = face_recognition.face_encodings(one_image)[0]

two_image = face_recognition.load_image_file("photos/two.jpg")
two_encoding = face_recognition.face_encodings(two_image)[0]

three_image = face_recognition.load_image_file("photos/three.jpg")
three_encoding = face_recognition.face_encodings(three_image)[0]

four_image = face_recognition.load_image_file("photos/four.jpg")
four_encoding = face_recognition.face_encodings(four_image)[0]

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
    
    rgb_small_frame = small_frame[:,:,::-1]
    #rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces (known_face_encoding,face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
    
    
    
    if cv2.waitKey(1) == ord('q'):  #button to close the webcam
      break 
    
    
cap.release()
cv2.destroyAllWindows()
