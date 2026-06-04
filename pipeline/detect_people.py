import cv2
import requests

from ultralytics import YOLO
from tracker import get_visitor_id
from emit import create_event

# Load YOLO model
model = YOLO("yolov8n.pt")

# Video path
video_path = r"C:\Users\aadis\Downloads\purplle-store-intelligence\CCTV Footage\CAM 3.mp4"

cap = cv2.VideoCapture(video_path)

cv2.namedWindow(
    "Purplle Person Detection",
    cv2.WINDOW_NORMAL
)

cv2.resizeWindow(
    "Purplle Person Detection",
    1920,
    1080
)

seen_visitors = set()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    person_count = 0

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])

            if class_id == 0:

                person_count += 1

                track_id = person_count

                visitor_id = get_visitor_id(track_id)

                if visitor_id not in seen_visitors:

                    seen_visitors.add(visitor_id)

                    event = create_event(
                        visitor_id=visitor_id,
                        camera_id="CAM3",
                        event_type="ENTRY",
                        zone="STORE"
                    )

                    try:

                        response = requests.post(
                            "http://127.0.0.1:8000/events/ingest",
                            json=event,
                            timeout=2
                        )

                        print("Event Sent:", event)
                        print("Status:", response.status_code)

                    except Exception as e:

                        print("API Error:", e)

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    visitor_id,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

    cv2.putText(
        frame,
        f"People Count: {person_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow(
        "Purplle Person Detection",
        frame
    )

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