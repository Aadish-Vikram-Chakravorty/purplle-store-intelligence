import cv2

video_path = r"C:\Users\aadis\Downloads\purplle-store-intelligence\CCTV Footage\CAM 3.mp4"

cap = cv2.VideoCapture(video_path)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("Width:", width)
print("Height:", height)

cap.release()