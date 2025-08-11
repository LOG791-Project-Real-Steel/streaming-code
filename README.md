> [!CAUTION]
> **⚠️ This repository is NOT maintained and is used for testing purposes only.**  
> It is **not part of the final solution** and should not be used in production.

![Status: Unmaintained](https://img.shields.io/badge/status-unmaintained-red?style=for-the-badge)
![Purpose: Testing Only](https://img.shields.io/badge/purpose-testing--only-orange?style=for-the-badge)
![Not Final](https://img.shields.io/badge/final--solution-NO-lightgrey?style=for-the-badge)

# Real-Time Video Processing with WebSockets

This repository contains a Python-based solution for real-time video processing using WebSockets. It enables you to stream video from an RTSP source or a video file, process each frame on the server, and display the processed frames on the client side using OpenCV. The system is designed to automatically reconnect if the connection is lost.

## Installation

1. Activate your Python environment (if you have one).
2. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Solutions

There is more than one solution here since iit's simple server mock code snippets to help use debug and test functionnalities related to sending video to the oculus quest 2 via websocket.

## 1. RTSP Test Server (`rtsp-test-server`)

Allowed Max to test video playback on the oculus quest 2 while developping the interface on it.

## Features

- **WebSocket-based API:** The code uses WebSockets to establish communication between the server and client, allowing real-time video streaming and processing.

- **Easy Setup:** Simply run the server and client scripts to start processing video frames. You can easily replace the RTSP link with your own source.

- **Customizable Image Processing:** The server processes video frames frame by frame, allowing you to implement various image processing techniques. In the provided code, frames are converted to grayscale, but you can customize this to fit your needs.

### Running it

> [!TIP]
> In the `rtsp-test-server/client.py`, there is a filde link to a video that will play on the oculus quest 2. You will most likely need to find a video yourself and modify the path in that file.

1. Go to the `rtsp-test-server` folder.
   ```bash
   cd rtsp-test-server
   ```

2. Run the server script:
   > [!NOTE]
   > This script runs the server that receives the video link from the client, processes each frame, and sends the processed frames back to the client.

   ```bash
   python3 server.py
   ```

3. Run the client script:
   > [!NOTE]
   > This script connects to the server, sends the video link to the server, receives the processed frames, and displays them using OpenCV.

   ```bash
   python3 client.py
   ```

## 2. Websocket Video Test Server (`websocket-video-test-server`)

> [!NOTE]
> These python scripts were helpful in testing the video display functionnality on the oculus quest 2 standalone via websocket. It's very similar to **RTSP Test Server** solution presented earlier. 

### Running it

1. Go to the `websocket-video-test-server` folder.
   ```bash
   websocket-video-test-server
   ```

> [!TIP]
> To test the streaming with webcam onto the oculus quest, run the `dummy_webcam_home_server.py` script.
>
> To test the streaming with a static video that loops non-stop, run the `dummy_home_server.py` script. It's mostly helpful to test that the video doesn't lag without having to be in front of the camera and moving.

2. Either run the first one:
   ```bash
   python3 dummy_webcam_home_server.py
   ```

   or, the second one:
   ```bash
   python3 dummy_home_server.py
   ```

3. Then, simply connect to it on port `8765` via localhost.

---

> Made with care by @Funnyadd, @ImprovUser, @cjayneb and @RaphaelCamara :heart:.
