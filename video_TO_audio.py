

from moviepy.editor import VideoFileClip

# Path to the video file
video_path = "/Users/vikramkumar/Desktop/Learn-AI-ML/OpenCv/video.mp4"

# Path to save the audio file
audio_path = "/Users/vikramkumar/Desktop/Learn-AI-ML/OpenCv/vikram_audio.mp3"

# Load the video file
video = VideoFileClip(video_path)

# Extract the audio
audio = video.audio

# Write the audio to a file
audio.write_audiofile(audio_path)

print(f"Audio extracted and saved to {audio_path}")
