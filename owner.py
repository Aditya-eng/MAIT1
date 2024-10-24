import cv2

# Initialize the camera
cam = cv2.VideoCapture(0)
ret, frame = cam.read()

if ret:
    cv2.imwrite("Documents/MAIT-Hackathon-main/room_owner.jpg", frame)  # Save the owner's image
    print("Room owner's picture saved as 'room_owner.jpg'")
cam.release()