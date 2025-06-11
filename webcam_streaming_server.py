import cv2
import asyncio
import websockets
import base64

# Might need to compress the messages and send them to make it better but for now, this works
# with the unity build. Need to find a way to directly communicate with the headset. Maybe via a publically available server...
async def send_frames(websocket, path):
    
    cap = cv2.VideoCapture(0)
    print("🔌 Client connected")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                continue
            _, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer).decode('utf-8')
            await websocket.send(jpg_as_text)
            await asyncio.sleep(0.03) # ~30fps 
    except websockets.exceptions.ConnectionClosed:
        print("🔌 Client disconnected")
    finally:
        cap.release()

async def main():
    async with websockets.serve(send_frames, "0.0.0.0", 8765): # means it runs on localhost
        print("✅ WebSocket server started on port 8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
