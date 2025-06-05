import asyncio
import websockets
import cv2
import base64
import numpy as np

async def receive_and_display_frames():
    uri = "ws://localhost:8080"  # WebSocket server URL
    frame_count = 0
    is_processing = False  # Flag to track if the client is busy processing a frame

    while True:
        try:
            async with websockets.connect(uri) as websocket:
                print("Connected to the server.")

                # Send the video file link to the server
                video_link = "C:/Users/MaxenceLord/LOG791/Streaming_Code/test_video.mkv"
                await websocket.send(video_link)
                print(f"Sent video link: {video_link}")

                while True:
                    if is_processing:
                        continue

                    # Receive a base64-encoded frame from the server
                    base64_frame = await websocket.recv()

                    if not base64_frame:
                        continue

                    is_processing = True
                    frame_count += 1
                    print(f"Received frame {frame_count}...")

                    try:
                        # Decode the base64 frame and display it
                        frame_data = base64.b64decode(base64_frame)
                        frame_np = np.frombuffer(frame_data, np.uint8)
                        frame = cv2.imdecode(frame_np, cv2.IMREAD_GRAYSCALE)
                        cv2.imshow("Frame", frame)

                        # Press 'q' to quit the display
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            print("Quitting display loop.")
                            break

                    except Exception as e:
                        print(f"Error decoding frame: {str(e)}")

                    is_processing = False

                # After breaking from the inner loop
                cv2.destroyAllWindows()

        except websockets.exceptions.ConnectionClosedError:
            print("Connection to the server closed. Reconnecting...")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"Error on the client: {str(e)}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(receive_and_display_frames())
