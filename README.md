# Human Detection App

This application utilizes the YOLOv5 model for detecting humans in videos or via a webcam feed. It's built using Python and Streamlit, offering a user-friendly interface to perform real-time human detection.

## Setup

1. **Installation**
   - Ensure you have Python installed.
   - Install the required libraries by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the App**
   - Run the app by executing:
     ```bash
     streamlit run app.py
     ```

## Usage

### Select Input Source
- Choose between detecting humans from a video file or a live webcam feed.

### Video Input
- Upload a video file (supported formats: mp4, avi).
- Click the "Start Tracking" button to begin human detection.
- The video will play, and detected humans will be outlined in red rectangles in real-time.
- The total count of detected humans will be displayed after the video finishes processing.

### Webcam Input
- Select the "Webcam" option to use your device's webcam.
- Click "Start Tracking" to initiate human detection from the live webcam feed.
- Detected humans will be outlined in red rectangles in real-time.
- The total count of detected humans will be displayed when you stop the detection process.
