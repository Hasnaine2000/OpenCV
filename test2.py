import cv2
import face_recognition
import os
import numpy as np

# Folder containing images
IMAGE_FOLDER = "photos"
IMAGE_NAMES = ["one.jpg", "two.jpg", "three.jpg", "four.jpg"]

# Dictionary to store encodings
face_encodings_dict = {}

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

        # Ensure the image is in uint8 format
        image_rgb = image_rgb.astype('uint8')

        # Get face encodings
        encodings = face_recognition.face_encodings(image_rgb)

        if encodings:
            face_encodings_dict[image_name] = encodings[0]  # Store first encoding
        else:
            print(f"No face found in {image_name}")
    
    except Exception as e:
        print(f"Error processing {image_name}: {e}")

# Print results
for name, encoding in face_encodings_dict.items():
    print(f"Stored encoding for {name}")
