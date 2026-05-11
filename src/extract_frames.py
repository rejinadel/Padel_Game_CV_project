import cv2
import os

# Paths
video_path = r'C:\Users\prashant\OneDrive\Desktop\TaskCV_project\data\videos\input_sample_video.mp4'  # Path to your video file
output_dir = r'C:\Users\prashant\OneDrive\Desktop\TaskCV_project\data\frames\extracted_frames'  # Path to save images

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Open the video file
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

# Get video FPS and frame count
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"Video FPS: {fps}")
print(f"Total Frames: {total_frames}")

# Frame interval logic
desired_fps = 2
frame_interval = int(fps // desired_fps) if desired_fps < fps else 1

# Extract frames
frame_count =0 
image_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        image_name = f"padel_frames_{image_count + 1}.jpg"  # <-- Updated filename here
        image_path = os.path.join(output_dir, image_name)
        cv2.imwrite(image_path, frame)
        print(f"Saved {image_name} at resolution {frame.shape[1]}x{frame.shape[0]}")
        image_count += 1

    frame_count += 1

cap.release()
print(" Video to image conversion complete.")