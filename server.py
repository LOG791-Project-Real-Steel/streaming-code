import asyncio
import websockets
import cv2
import base64


async def process_video(websocket):
    try:
        print("Client connected.")

        video_link = await websocket.recv()
        if not video_link:
            raise ValueError("Empty video link received")
        print("Received video link:", video_link)

        cap = cv2.VideoCapture(video_link)
        if not cap.isOpened():
            raise IOError("Failed to open video file: " + video_link)

        frame_count = 0
        isProcessing = False
        processing_delay = 0.0

        while True:
            if isProcessing:
                await asyncio.sleep(processing_delay)
                continue

            ret, frame = cap.read()
            if not ret:
                break

            isProcessing = True

            frame_count += 1
            print(f"Processing frame {frame_count}...")

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, frame_data = cv2.imencode('.jpg', gray_frame)
            base64_frame = base64.b64encode(frame_data).decode("utf-8")

            await websocket.send(base64_frame)
            await asyncio.sleep(processing_delay)
            isProcessing = False

        cap.release()
        print("Video processing complete. Closing connection.")
        await websocket.close()

    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected. Waiting for a new connection...")
    except Exception as e:
        print(f"Error on the server: {str(e)}")


async def main():
    print("Starting WebSocket server...")
    print("=== GOOD VERSION OF SERVER.PY ===")
    async with websockets.serve(process_video, "localhost", 8080):
        print("WebSocket server started.")
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
