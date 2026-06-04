import cv2
from ultralytics import YOLO

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

while True:

    ret, frame = cap.read()
    print("Original Frame Shape:", frame.shape)

    if not ret:
        break

    # Run YOLO detection
    results = model(frame)
    print("YOLO Input Shape:", results[0].orig_shape)

    person_count = 0

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])

            # Person class
            if class_id == 0:

                person_count += 1

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