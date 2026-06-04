# Purplle Store Intelligence System

AI-powered retail analytics platform built for the Purplle Tech Challenge 2026.

## Overview

This project processes CCTV footage from retail stores, detects visitors using YOLOv8, generates structured visitor events, stores them in a database, and exposes analytics through FastAPI endpoints.

The system is designed to provide store intelligence metrics such as visitor counts, funnel analysis, anomaly detection, and event tracking.

---

## Features

* Visitor detection using YOLOv8
* Visitor tracking and ID assignment
* Event generation pipeline
* SQLite-based event storage
* Metrics API
* Funnel analytics API
* Anomaly detection API
* Health monitoring endpoint
* Swagger API documentation
* Dockerized deployment
* Automated API tests using Pytest

---

## Project Structure

```text
app/
├── main.py
├── database.py
├── models.py
├── funnel.py
└── anomalies.py

pipeline/
├── detect_people.py
├── tracker.py
└── emit.py

docs/
├── DESIGN.md
└── CHOICES.md

tests/
└── test_api.py
```

---

## Technology Stack

* Python
* FastAPI
* SQLite
* YOLOv8
* OpenCV
* Docker
* Pytest

---

## API Endpoints

### Health Check

GET /health

Returns service health status.

### Metrics

GET /metrics

Returns event statistics including entries and exits.

### Funnel

GET /funnel

Returns visitor funnel analytics and conversion rate.

### Anomalies

GET /anomalies

Returns detected operational anomalies.

### Event Ingestion

POST /events/ingest

Stores visitor events in the database.

---

## Running the Application

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start API

```bash
uvicorn app.main:app --reload
```

### Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Running Tests

```bash
python -m pytest
```

---

## Design Documentation

See:

* docs/DESIGN.md
* docs/CHOICES.md

for architecture decisions, trade-offs, and AI-assisted development notes.

---

## Future Improvements

* Multi-camera visitor tracking
* Re-identification across cameras
* Real-time dashboard
* PostgreSQL backend
* Advanced anomaly detection
* Queue analytics

---

## Challenge Submission

Built for Purplle Tech Challenge 2026.
