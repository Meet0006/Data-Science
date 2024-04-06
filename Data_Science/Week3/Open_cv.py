import cv2

# Get the index of the front camera
camera_index = 0  # Adjust this value if necessary

# Open the front camera
cap = cv2.VideoCapture(camera_index)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Front camera opened successfully.")

# Release the camera when done
cap.release()