# PROMPT:
# Generate FastAPI tests for health, metrics and ingest endpoints.
#
# CHANGES MADE:
# Adjusted endpoint names to match this project.
# Added custom assertions after manual testing.

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200


def test_funnel():
    response = client.get("/funnel")
    assert response.status_code == 200


def test_anomalies():
    response = client.get("/anomalies")
    assert response.status_code == 200