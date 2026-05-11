from ultralytics import YOLO

# load trained model
model = YOLO(r"C:\Users\prashant\OneDrive\Desktop\TaskCV_project\best.pt")

# run tracking
results = model.track(
    source=r"C:\Users\prashant\OneDrive\Desktop\TaskCV_project\data\videos\input_sample_video.mp4",
    save=True,
    conf=0.25,
    persist=True   # IMPORTANT: keeps IDs consistent
)