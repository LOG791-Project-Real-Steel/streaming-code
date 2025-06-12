import asyncio
import websockets
import os
import random

VIDEO_FOLDER = "./videos"  # Folder with your video files
CHUNK_SIZE = 1024 * 64      # 64KB per chunk
PORT = 8765

async def send_video(websocket, path):
    while True:
        # Pick a random video
        video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(".mp4")]
        selected_video = os.path.join(VIDEO_FOLDER, random.choice(video_files))

        print(f"Streaming: {selected_video}")
        with open(selected_video, "rb") as f:
            chunk = f.read(CHUNK_SIZE)
            while chunk:
                try:
                    await websocket.send(chunk)
                    await asyncio.sleep(0.01)  # simulate stream pacing
                    chunk = f.read(CHUNK_SIZE)
                except websockets.ConnectionClosed:
                    print("Client disconnected.")
                    return
        print(f"Finished streaming {selected_video}, restarting.")

async def main():
    async with websockets.serve(send_video, "0.0.0.0", PORT):
        print(f"WebSocket server started on ws://0.0.0.0:{PORT}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
