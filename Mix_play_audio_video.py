
import cv2
import pygame
import threading

# Initialize Pygame mixer
pygame.mixer.init()

# Load the video file
video_path = "/Users/vikramkumar/Desktop/Learn-AI-ML/OpenCv/video.mp4"
cap = cv2.VideoCapture(video_path)

# Extract audio from the video file (if audio is embedded)
# For simplicity, you can use a separate audio file if needed
audio_path = "/Users/vikramkumar/Desktop/Learn-AI-ML/OpenCv/vikram_audio.mp3"
pygame.mixer.music.load(audio_path)

# Define a function to play audio
def play_audio():
    pygame.mixer.music.play()

# Start a new thread to play audio
audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

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
    # Stop the audio playback
    pygame.mixer.music.stop()
