# Purplle Store Intelligence System - Design Document

## Overview

The Purplle Store Intelligence System is designed to process retail store CCTV footage and generate actionable business insights.

The system consists of two major layers:

1. Computer Vision Layer
2. Analytics API Layer

The Computer Vision layer detects customers from CCTV footage using YOLOv8 and generates visitor events.

The Analytics API layer stores events, computes business metrics, detects anomalies, and exposes insights through REST APIs.

---

## Architecture

CCTV Footage
↓
YOLOv8 Detection
↓
Event Generation
↓
SQLite Database
↓
FastAPI Service
↓
Metrics / Funnel / Anomalies APIs

---

## Components

### Detection Layer

File:
pipeline/detect_people.py

Responsibilities:

* Read CCTV footage
* Run YOLOv8 inference
* Detect persons
* Draw bounding boxes
* Count detected visitors

Output:

* Visitor observations
* Entry and exit events

---

### Event Storage Layer

Files:

* app/database.py
* app/models.py

Responsibilities:

* Store visitor events
* Maintain event history
* Provide analytics queries

Database:

SQLite

Table:

events

Fields:

* visitor_id
* camera_id
* event_type
* zone
* timestamp

---

### API Layer

File:

app/main.py

Responsibilities:

* Event ingestion
* Metrics reporting
* Funnel analytics
* Health monitoring
* Anomaly reporting

Endpoints:

GET /

GET /health

GET /metrics

GET /funnel

GET /anomalies

POST /events/ingest

---

### Metrics Layer

File:

app/database.py

Responsibilities:

* Total event count
* Entry count
* Exit count

Business Value:

Provides store traffic visibility.

---

### Funnel Layer

File:

app/funnel.py

Responsibilities:

* Count visitors
* Count completed journeys
* Calculate drop-offs

Business Value:

Measures customer conversion opportunities.

---

### Anomaly Layer

File:

app/anomalies.py

Responsibilities:

* Detect unusual traffic
* Detect inactivity
* Detect crowd build-up situations

Business Value:

Provides operational alerts.

---

## Technology Choices

Backend:
FastAPI

Database:
SQLite

Computer Vision:
YOLOv8

Language:
Python

Containerisation:
Docker

---

## Scalability Considerations

Future improvements include:

* Multi-camera tracking
* Re-identification models
* PostgreSQL database
* Redis caching
* Kafka event streaming
* Real-time dashboard

---

## North Star Metric

Offline Store Conversion Rate

Conversion Rate =
Customers Completing Purchase /
Total Unique Visitors

All system components are designed to improve the accuracy and usefulness of this business metric.
