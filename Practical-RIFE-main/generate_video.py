import cv2
import os

# Set paths to the frames
frame1_path = '../TestingFolder/1.png'
frame2_path = '../TestingFolder/2.png'

# Load the images
frame1 = cv2.imread(frame1_path)
frame2 = cv2.imread(frame2_path)

# Define the target size (width, height)
target_width = 1200  # Change to desired width
target_height = 700  # Change to desired height

# Resize frames to the target size
resized_frame1 = cv2.resize(frame1, (target_width, target_height))
resized_frame2 = cv2.resize(frame2, (target_width, target_height))

# Create a Video Writer Object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 1  # Frames per second (adjust as needed)
output_video_path = 'output.mp4'
video = cv2.VideoWriter(output_video_path, fourcc, fps, (target_width, target_height))

# Write Frames to Video
video.write(resized_frame1)
video.write(resized_frame2)

# Release the Video Writer
video.release()

# Run RIFE inference
os.system(f"python inference_video.py --video {output_video_path} --multi=2 --output ../abc.mp4 ")
