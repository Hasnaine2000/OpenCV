import cv2
import face_recognition
import os
import numpy as np

# Folder containing images
IMAGE_FOLDER = "photos"
IMAGE_NAMES = ["one.jpg", "two.jpg", "three.jpg", "four.jpg"]

# Dictionary to store encodings
known_face_encodings = []
known_face_names = []

for image_name in IMAGE_NAMES:
    image_path = os.path.join(IMAGE_FOLDER, image_name)
    
    try:
        # Read image with OpenCV
        image_bgr = cv2.imread(image_path)
        
        # Check if image was loaded correctly
        if image_bgr is None:
            print(f"Error: Could not read {image_name}. Check file format and path.")
            continue
        
        # Convert BGR (OpenCV format) to RGB (face_recognition format)
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        
        # Get face encodings
        encodings = face_recognition.face_encodings(image_rgb)
        
        if encodings:
            known_face_encodings.append(encodings[0])  # Store first encoding
            known_face_names.append(image_name)  # Store corresponding name
        else:
            print(f"No face found in {image_name}")
    
    except Exception as e:
        print(f"Error processing {image_name}: {e}")

# Start video capture
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture frame from camera. Exiting...")
        break
    
    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        # Find the best match
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances) if face_distances.size > 0 else None
        
        if best_match_index is not None and matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        print(f"{name} is present")
    
    # Show the frame
    cv2.imshow("Video", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()