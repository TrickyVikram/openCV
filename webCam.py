import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
    else:
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the original and grayscale frames
        cv2.imshow("Original", frame)
        cv2.imshow("Grayscale", gray_frame)

        # Wait for any key to be pressed to close all windows
        wait = cv2.waitKey(0)

        if wait:
            print("Saved")
            cv2.imwrite("/Users/vikramkumar/Desktop/Learn-AI-ML/OpenCv/gray_vikram.jpg", gray_frame)  # Save the grayscale frame with the correct extension
        else:
            print("Not saved")

        # Close all windows
        cv2.destroyAllWindows()

    # Release the webcam
    cap.release()