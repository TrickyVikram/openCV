import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Read a frame from the webcam
ret, frame = cap.read()

# Display the original frame
cv2.imshow("Original", frame)

# Wait for any key to be pressed to close all windows
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

# Release the webcam
cap.release()
