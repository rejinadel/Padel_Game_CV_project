# Padel Game Analytics — Shot Classification System

## Project Overview

This project is an AI-powered sports analytics system designed to analyze padel and tennis match videos and convert them into structured gameplay insights using computer vision and deep learning techniques.

The system detects and tracks:

* Players
* Ball
* Racket

It further performs:

* Shot event detection
* Shot classification (Forehand, Backhand, Smash/Overhead)
* CSV generation for analytics
* Visualization-ready outputs for Power BI and Python dashboards

The complete pipeline transforms raw sports footage into meaningful, data-driven performance analytics.

---

# System Pipeline

```text
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
```

---

# Model Details

## Model

* YOLOv8 Custom-Trained Model
* Framework: Ultralytics

## Classes

* Player
* Ball
* Racket

---

# Training Results

## Overall Performance

| Metric    | Value  |
| --------- | ------ |
| Precision | 0.8969 |
| Recall    | 0.8387 |
| mAP@50    | 0.8684 |
| mAP@50-95 | 0.4940 |
| Fitness   | 0.4940 |

---

## Per-Class Performance

| Class  | mAP   |
| ------ | ----- |
| Player | 0.337 |
| Ball   | 0.820 |
| Racket | 0.324 |

---

## Speed Performance

| Stage       | Time    |
| ----------- | ------- |
| Preprocess  | 0.36 ms |
| Inference   | 4.71 ms |
| Postprocess | 4.45 ms |

---

# Dataset Preparation

* Extracted frames from match video
* Annotated 401 images manually
* Labels:

  * Player
  * Ball
  * Racket

The dataset was used to train the YOLOv8 model for sports-specific object detection.

---

# Shot Detection Logic

Shot events are detected using rule-based motion analysis techniques including:

* Ball movement (dx, dy)
* Velocity spikes
* Frame gap filtering
* Position changes

A shot event is recorded only when significant movement is detected to avoid duplicate detections.

---

# Shot Classification Rules

| Shot Type        | Logic                                    |
| ---------------- | ---------------------------------------- |
| Forehand         | Ball moves in dominant forward direction |
| Backhand         | Opposite directional movement            |
| Smash / Overhead | High position with fast downward motion  |
| Serve            | Initial low-motion event                 |

---

# Output Generated

## CSV Format

```text
timestamp,frame,shot_type,ball_x,ball_y,movement
```

---

## Files Generated

```text
output/
├── shot_events.csv
├── shot_summary.csv
├── dashboard.png
```

---

# Visual Analytics

The system generates:

* Shot distribution bar charts
* Shot percentage donut charts
* Shot timeline analysis
* KPI summary cards
* Performance trend analysis

These outputs are directly compatible with Power BI dashboards and Python visualization libraries.

---

# GPU Acceleration

For faster training and inference, GPU-based execution is recommended.

## Supported Platforms

* Google Colab (Free GPU)
* Google Cloud (Scalable GPU Virtual Machines)

---

## Why GPU?

| Task             | CPU   | GPU                   |
| ---------------- | ----- | --------------------- |
| YOLO inference   | Slow  | Fast                  |
| Video processing | Heavy | Optimized             |
| Model training   | Hours | Significantly Reduced |

GPU acceleration enables faster video processing, real-time inference capability, and efficient deep learning model training.

---

# Tech Stack

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* Pandas
* Matplotlib
* Seaborn

---

# Setup Instructions

## 1. Create Environment (Anaconda Recommended)

```bash
conda create -n padel_cv python=3.10 -y
conda activate padel_cv
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run Pipeline

```bash
python pipeline.py
```

---

## 4. Generate Visualization

```bash
python visualization.py
```

---

# Project Structure

```text
TaskCV_project/
│
├── data/
├── models/
├── output/
├── src/
│   ├── pipeline.py
│   ├── visualization.py
│   └── additional modules
│
├── best.pt
├── requirements.txt
└── README.md
```

---

# Challenges Faced

* Small object detection (ball tracking)
* Motion blur during fast rallies
* Duplicate shot detection filtering
* Tracking stability across frames
* Designing rule-based classification logic

---

# Results

The project successfully:

* Detects real match gameplay events
* Converts raw video into structured datasets
* Generates analytics-ready outputs
* Supports coaching insights and performance evaluation

---

# Future Improvements

* Player-specific shot attribution
* Real-time streaming analytics
* Deep learning-based shot classification
* Rally segmentation (point-level analysis)
* Streamlit interactive dashboard

---

# Conclusion

This project demonstrates a complete end-to-end AI sports analytics pipeline combining:

* Computer Vision
* Deep Learning (YOLOv8)
* Object Tracking
* Rule-Based Reasoning
* Data Analytics

The system transforms raw padel and tennis match videos into actionable insights suitable for sports performance analysis and visualization.
