from ultralytics import YOLO
import cv2
import pandas as pd
import math
import os
MODEL_PATH = r"C:\Users\prashant\OneDrive\Desktop\TaskCV_project\best.pt"

VIDEO_PATH = (
    r"C:\Users\prashant\OneDrive\Desktop\TaskCV_project"
    r"\data\videos\input_sample_video.mp4"
)

OUTPUT_DIR = (
    r"C:\Users\prashant\OneDrive\Desktop\TaskCV_project"
    r"\output"
)
os.makedirs(OUTPUT_DIR, exist_ok=True)
# LOAD MODEL
model = YOLO(MODEL_PATH)
print("MODEL LOADED SUCCESSFULLY")

# VIDEO CAPTURE
cap = cv2.VideoCapture(VIDEO_PATH)
fps = cap.get(cv2.CAP_PROP_FPS)

# STORAGE
shot_events = []

prev_ball_x = None
prev_ball_y = None

frame_id = 0
last_shot_frame = -100

forehand_count = 0
backhand_count = 0


# TRACKING LOOP

results = model.track(
    source=VIDEO_PATH,
    stream=True,
    persist=True,
    tracker="bytetrack.yaml",
    conf=0.35,
    imgsz=640
)

print("STARTING SHOT ANALYSIS")

for r in results:

    frame_id += 1

    timestamp_sec = frame_id / fps
    minutes = int(timestamp_sec // 60)
    seconds = int(timestamp_sec % 60)
    timestamp = f"{minutes:02}:{seconds:02}"

    ball_detected = False
    ball_x = None
    ball_y = None
    current_shot = None

    if r.boxes is not None:

        for box in r.boxes:

            cls = int(box.cls[0])
            class_name = model.names[cls]

            if class_name.lower() == "ball":

                x1, y1, x2, y2 = box.xyxy[0].tolist()

                ball_x = int((x1 + x2) / 2)
                ball_y = int((y1 + y2) / 2)

                ball_detected = True
                break

    if ball_detected and prev_ball_x is not None:

        dx = ball_x - prev_ball_x
        dy = ball_y - prev_ball_y

        movement = math.sqrt(dx**2 + dy**2)

        cooldown = int(fps * 0.6)

        if (
            movement > 16
            and abs(dx) > 6
            and frame_id - last_shot_frame > cooldown
        ):

            if dx > 0:
                current_shot = "Forehand"
                forehand_count += 1
            else:
                current_shot = "Backhand"
                backhand_count += 1

            shot_events.append({
                "timestamp": timestamp,
                "frame": frame_id,
                "shot_type": current_shot,
                "movement": round(movement, 2)
            })

            last_shot_frame = frame_id

    if ball_detected:
        prev_ball_x = ball_x
        prev_ball_y = ball_y

    if frame_id % 200 == 0:
        print(f"Processed {frame_id} frames...")


# RELEASE
cap.release()

print("VIDEO PROCESSING COMPLETED")
# DATAFRAME

df = pd.DataFrame(shot_events).drop_duplicates()


# SAVE CSV

events_csv = os.path.join(OUTPUT_DIR, "shot_events.csv")

df.to_csv(events_csv, index=False)


# SUMMARY

summary_df = pd.DataFrame({
    "Shot_Type": ["Forehand", "Backhand"],
    "Count": [forehand_count, backhand_count]
})

summary_csv = os.path.join(OUTPUT_DIR, "shot_summary.csv")

summary_df.to_csv(summary_csv, index=False)

# OUTPUT

print("\nSHOT ANALYSIS COMPLETED")
print(summary_df)

print("\nFILES SAVED:")
print(events_csv)
print(summary_csv)