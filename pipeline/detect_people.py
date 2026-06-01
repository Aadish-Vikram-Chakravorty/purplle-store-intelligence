import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Video path
video_path = r"C:\Users\aadis\Downloads\purplle-store-intelligence\CCTV Footage\CAM 3.mp4"

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    for result in results:
        for box in result.boxes:

            class_id = int(box.cls[0])

            # COCO class 0 = person
            if class_id == 0:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    "Person",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

cv2.imshow("Purplle Person Detection", frame)

key = cv2.waitKey(1)

if key == ord("q"):
    break

if cv2.getWindowProperty(
    "Purplle Person Detection",
    cv2.WND_PROP_VISIBLE
) < 1:
    break

cap.release()
cv2.destroyAllWindows()