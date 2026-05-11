Padel Game Analytics — Shot Classification System


Project Overview

This project is an AI-powered sports analytics system that analyzes padel/tennis match videos and converts them into structured gameplay insights.

It detects and tracks:

Players
Ball
Racket

It then performs:

Shot event detection
Shot classification (Forehand, Backhand, Smash/Overhead)
CSV generation for analytics
Visualization-ready outputs for Power BI / Python dashboards

The system transforms raw sports video into data-driven performance insights using computer vision and deep learning.

System Pipeline
Input Video
   ↓
Frame Extraction
   ↓
Annotation (401 Images)
   ↓
YOLOv8 Training
   ↓
Object Detection (Player / Ball / Racket)
   ↓
Tracking (ByteTrack-style)
   ↓
Shot Event Detection
   ↓
Shot Classification
   ↓
CSV + Visualization

Model Details
Model: YOLOv8 custom-trained
Framework: Ultralytics
Classes:
Player
Ball
Racket

Training Results
Overall Performance
Metric	Value
Precision	0.8969
Recall	0.8387
mAP@50	0.8684
mAP@50-95	0.4940
Fitness	0.4940

Per-Class Performance
Class	mAP
Player	0.337
Ball	0.820
Racket	0.324

Speed Performance
Stage	Time
Preprocess	0.36 ms
Inference	4.71 ms
Postprocess	4.45 ms

Dataset Preparation
Extracted frames from match video
Annotated 401 images manually
Labels:
Player
Ball
Racket

This dataset was used to train the YOLOv8 model for sports-specific detection.

Shot Detection Logic

Shot events are detected using rule-based motion analysis:

Ball movement (dx, dy)
Velocity spikes
Frame gap filtering
Position changes

A shot is registered only when significant motion is detected to avoid duplicates.

Shot Classification Rules
Shot Type	Logic
Forehand	Ball moves in dominant forward direction
Backhand	Opposite directional movement
Smash / Overhead	High position + fast downward motion
Serve	Initial low-motion event

Output Generated
CSV Format
timestamp,frame,shot_type,ball_x,ball_y,movement
Files Generated
output/
 ├── shot_events.csv
 ├── shot_summary.csv
 ├── dashboard.png
📈 Visual Analytics

The system generates:

Shot distribution (bar chart)
Shot percentage (donut chart)
Shot timeline analysis
KPI summary cards
Performance trends

These outputs are directly usable in Power BI dashboards.

GPU Acceleration

For faster processing, GPU-based execution is recommended:

Google Colab (Free GPU)
Google Cloud (Scalable GPU VMs)
Why GPU?
Task	CPU	GPU
YOLO inference	slow	fast
Video processing	heavy	optimized
Training	hours	significantly reduced

Tech Stack
Python
YOLOv8 (Ultralytics)
OpenCV
Pandas
Matplotlib
Seaborn


Setup Instructions
1. Create Environment (Anaconda Recommended)
conda create -n padel_cv python=3.10 -y
conda activate padel_cv
2. Install Dependencies
pip install -r requirements.txt
3. Run Pipeline
python pipeline.py
4. Generate Visualization
python visualization.py

Project Structure
TaskCV_project/
│
├── data/
├── models/
├── output/
├── src/
│   ├── pipeline.py
│   ├── visualization.py and so on modules
│
├── best.pt
├── requirements.txt
└── README.md

Challenges Faced
Small object detection (ball tracking)
Motion blur during fast rallies
Duplicate shot detection filtering
Tracking stability across frames
Designing rule-based classification logic


Results
Successfully detects real match gameplay events
Converts raw video → structured dataset
Enables analytics-ready outputs
Works for coaching and performance evaluation

Future Improvements
Player-specific shot attribution
Real-time streaming analytics
Deep learning-based shot classification
Rally segmentation (point-level analysis)
Streamlit interactive dashboard

Conclusion

This project demonstrates a complete end-to-end AI sports analytics pipeline combining:

Computer Vision
Deep Learning (YOLOv8)
Object Tracking
Rule-based reasoning
Data Analytics

It transforms raw padel match videos into actionable insights for performance analysis and visualization.