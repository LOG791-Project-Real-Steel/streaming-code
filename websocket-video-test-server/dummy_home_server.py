import asyncio
import websockets
import os
import random
import cv2
import base64

# Resolve the absolute path to the "video" folder
VIDEO_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "video")
PORT = 8765
FPS = 30  # controls stream rate

async def send_video(websocket):
    while True:
        # Pick a random video file
        video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith((".mp4", ".mov", ".avi"))]
        if not video_files:
            print("No video files found in folder:", VIDEO_FOLDER)
            return

        selected_video = os.path.join(VIDEO_FOLDER, random.choice(video_files))
        print(f"Streaming video: {selected_video}")

        cap = cv2.VideoCapture(selected_video)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break  # end of video

            # Resize frame for performance (optional)
            frame = cv2.resize(frame, (640, 360))

            # Encode frame as JPEG
            success, buffer = cv2.imencode(".jpg", frame)
            if not success:
                continue

            # Convert to base64
            b64 = base64.b64encode(buffer).decode("utf-8")

            try:
                await websocket.send(b64)
                await asyncio.sleep(1 / FPS)
            except websockets.ConnectionClosed:
                print("Client disconnected.")
                cap.release()
                return

        cap.release()
        print("Restarting with a new random video.")

async def handler(websocket, path):
    await send_video(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", PORT):
        print(f"WebSocket server listening on ws://0.0.0.0:{PORT}")
        await asyncio.Future()  # keep running

if __name__ == "__main__":
    asyncio.run(main())
