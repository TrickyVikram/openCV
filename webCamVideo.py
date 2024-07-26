import cv2
# Open the video file
cap = cv2.VideoCapture("/Users/vikramkumar/Desktop/Learn-AI-ML/OpenCv/video.mp4")

# Check if the video was successfully opened
if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    # Read until the video is completed
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if ret:
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            
            # Press 'q' on the keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    # When everything is done, release the video capture object
    cap.release()
    # Close all OpenCV windows
    cv2.destroyAllWindows()