from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import cv2
import numpy as np
from io import BytesIO
import subprocess

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/upload', methods=['POST'])
def upload_files():
    print('Function called')

    # Retrieve and print the dropdown value
    dropdown_value = request.form.get('dropdown')
    print(f"Dropdown value received: {dropdown_value}")

    if 'frame1' not in request.files or 'frame2' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    frame1_file = request.files['frame1']
    frame2_file = request.files['frame2']

    if frame1_file.filename == '' or frame2_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Convert file-like objects to numpy arrays
    frame1_np = np.frombuffer(frame1_file.read(), np.uint8)
    frame2_np = np.frombuffer(frame2_file.read(), np.uint8)

    # Decode the images
    frame1 = cv2.imdecode(frame1_np, cv2.IMREAD_COLOR)
    frame2 = cv2.imdecode(frame2_np, cv2.IMREAD_COLOR)

    if frame1 is None or frame2 is None:
        return jsonify({"error": "Error decoding images"}), 400

    # Define the target size (width, height)
    target_width = 1200  # Change to desired width
    target_height = 700  # Change to desired height

    # Resize frames to the target size
    resized_frame1 = cv2.resize(frame1, (target_width, target_height))
    resized_frame2 = cv2.resize(frame2, (target_width, target_height))

    # Create a Video Writer Object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 1  # Frames per second (adjust as needed)
    output_video_path = 'output1.mp4'
    video = cv2.VideoWriter(output_video_path, fourcc, fps, (target_width, target_height))

    # Write Frames to Video
    video.write(resized_frame1)
    video.write(resized_frame2)

    # Release the Video Writer
    video.release()

    # Run RIFE inference
    os.system(f"python inference_video.py --video {output_video_path} --multi={dropdown_value} --output ../result.mp4")

    return jsonify({"message": "Files uploaded and processed successfully"})

if __name__ == '__main__':
    app.run(debug=True)
