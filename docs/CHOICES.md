# Architectural Decisions and Trade-offs

This document records the key engineering decisions made during the development of the Purplle Store Intelligence System.

---

# Decision 1: YOLOv8 vs Traditional Computer Vision

## Problem

The system needs to detect customers from CCTV footage reliably.

## Options Considered

### Option A

OpenCV Background Subtraction

Pros:

* Fast
* Lightweight

Cons:

* Sensitive to lighting changes
* Poor performance with occlusions
* High false positives

### Option B

YOLOv8

Pros:

* High person detection accuracy
* Handles different viewing angles
* Robust to lighting variation
* Easy integration with Python

Cons:

* Higher compute cost

## Final Choice

YOLOv8

## Reasoning

Accuracy is more important than inference speed for this challenge.

YOLOv8 provides significantly better detection quality and reduces false detections compared to traditional computer vision approaches.

---

# Decision 2: SQLite vs PostgreSQL

## Problem

The system requires persistent event storage.

## Options Considered

### Option A

SQLite

Pros:

* Zero configuration
* Simple setup
* Lightweight
* Ideal for local development

Cons:

* Limited scalability

### Option B

PostgreSQL

Pros:

* Production ready
* Better concurrency
* Better scalability

Cons:

* Additional infrastructure
* More setup complexity

## Final Choice

SQLite

## Reasoning

The challenge focuses on analytics logic rather than database scaling.

SQLite allows rapid development while keeping deployment simple.

For production deployment PostgreSQL would be preferred.

---

# Decision 3: Rule-Based Anomaly Detection vs Machine Learning

## Problem

The system needs to identify unusual store activity.

## Options Considered

### Option A

Machine Learning Anomaly Detection

Pros:

* Learns patterns automatically

Cons:

* Requires historical data
* Higher implementation complexity
* Harder to explain

### Option B

Rule-Based Detection

Pros:

* Easy to implement
* Easy to debug
* Transparent behaviour

Cons:

* Less adaptive

## Final Choice

Rule-Based Detection

## Reasoning

Challenge datasets are relatively small.

Rule-based detection provides deterministic and explainable results while reducing development time.

---

# AI Assistance Usage

AI tools were used to:

* Generate implementation alternatives
* Compare technology choices
* Review API structure
* Review database schema
* Identify edge cases
* Generate initial documentation drafts

All generated outputs were manually reviewed, modified, tested, and integrated into the final solution.

The final architectural decisions were made after evaluating implementation complexity, accuracy, and business impact.
