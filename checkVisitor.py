import face_recognition
import cv2
import os

# Load the room owner's picture
owner_image = face_recognition.load_image_file("Documents/MAIT-Hackathon-main/room_owner.jpg")
owner_encodings = face_recognition.face_encodings(owner_image)

# Ensure that a face is detected in the owner's image
if len(owner_encodings) > 0:
    owner_encoding = owner_encodings[0]
else:
    print("No face detected in the owner's image.")
    exit()  # Exit the script if no face is found

# Capture the picture of the person trying to unlock the door
cam = cv2.VideoCapture(0)
ret, frame = cam.read()

if ret:
    # Find the next available filename (e.g., 1.jpg, 2.jpg, etc.)
    i = 1
    while os.path.exists(f"Documents/MAIT-Hackathon-main/{i}.jpg"):
        i += 1
    visitor_path = f"Documents/MAIT-Hackathon-main/{i}.jpg"

    # Save the visitor's image with the new filename
    cv2.imwrite(visitor_path, frame)
    cam.release()

    # Load the captured image
    visitor_image = face_recognition.load_image_file(visitor_path)
    visitor_encodings = face_recognition.face_encodings(visitor_image)

    # Compare faces
    if visitor_encodings:
        visitor_encoding = visitor_encodings[0]
        results = face_recognition.compare_faces(
            [owner_encoding], visitor_encoding)

        if results[0]:
            print(f"ROOM OWNER. DOOR UNLOCKED. Saved as {visitor_path}")
            # You can add the code to unlock the door here
        else:
            print(f"Visitor DETECTED. Image saved as {visitor_path}")
            # Notify the owner and keep the door locked
    else:
        print("No face detected in the captured image.")
else:
    print("Failed to capture image.")
