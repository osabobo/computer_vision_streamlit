import cv2
import numpy as np
import streamlit as st
import tempfile
import os
import torch
from PIL import Image

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Function to detect humans in a frame using YOLOv5
def detectHumans(frame):
    img = Image.fromarray(frame)
    results = model(img)

    # Extract bounding boxes and class labels for humans
    boxes = results.xyxy[0]
    humans = boxes[boxes[:, 5] == 0][:, :4].detach().numpy()

    # Count the number of humans detected
    count = len(humans)

    for (x_min, y_min, x_max, y_max) in humans:
        x_min, y_min, x_max, y_max = int(x_min), int(y_min), int(x_max), int(y_max)
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)

    return frame, count



def main():
    st.title("Human Detection App")
    input_source = st.sidebar.selectbox("Select Input Source", ("Video", "Webcam"))

    if input_source == "Video":
        # Upload a video file
        video_file = st.file_uploader("Upload a video file", type=["mp4", "avi"], accept_multiple_files=False)

        if video_file is not None:
            # Save the video file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_filename = temp_file.name
                temp_file.write(video_file.read())

            # Open the video file
            video = cv2.VideoCapture(temp_filename)

            if st.sidebar.button("Start Tracking"):
                stframe = st.empty()
                count = 0

                # Play the video
                while True:
                    ret, frame = video.read()
                    if not ret:
                        break

                    # Detect humans in the frame and get the count
                    transformed_frame, current_count = detectHumans(frame)

                    # Accumulate the count
                    count += current_count

                    # Display the transformed frame in Streamlit
                    stframe.image(transformed_frame, channels="BGR")

                # Release the video file
                video.release()

                # Delete the temporary file
                os.remove(temp_filename)

                # Display the total count
                st.write("Total number of humans detected:", count)

if __name__ == '__main__':
    main()
