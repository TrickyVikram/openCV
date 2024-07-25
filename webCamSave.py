# video capture using webcam

import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is the default camera

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the original frame
        cv2.imshow("Webcam Feed", frame)

        # Wait for key press
        key = cv2.waitKey(1) & 0xFF

        # If the 's' key is pressed, save the grayscale image
        if key == ord('s'):
            print("Saved")
            cv2.imwrite("/Users/vikramkumar/Desktop/Learn-AI-ML/OpenCv/gray_vikram.jpg", gray_frame)  # Save the grayscale frame with the correct extension
            cv2.imshow("Grayscale", gray_frame)

        # If the 'q' key is pressed, exit the loop
        elif key == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()
