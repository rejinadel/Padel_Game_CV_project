from ultralytics import YOLO


# 1. LOAD MODEL

model = YOLO(r"C:\Users\prashant\OneDrive\Desktop\TaskCV_project\best.pt")


# 2. RUN INFERENCE (STREAM MODE = NO MEMORY CRASH)

results = model.predict(
    source=r"C:\Users\prashant\OneDrive\Desktop\TaskCV_project\data\videos\input_sample_video.mp4",
    stream=True,        # IMPORTANT: prevents RAM crash
    save=True,          # saves output video
    conf=0.25,          # confidence threshold
    imgsz=512,          # reduces memory usage (important for long videos)
    device="cpu"        # safe default (remove if using GPU)
)


# 3. PROCESS RESULTS FRAME-BY-FRAME

for r in results:
    boxes = r.boxes  # detections per frame

    # OPTIONAL DEBUG (you can uncomment if needed)
    # print(boxes)