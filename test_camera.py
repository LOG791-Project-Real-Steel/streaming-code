import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Cannot open webcam")
else:
    print("✅ Webcam opened")
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
    else:
        print("✅ Frame grabbed")
cap.release()
