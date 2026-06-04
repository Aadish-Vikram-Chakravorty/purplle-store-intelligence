from fastapi import FastAPI

from app.database import create_tables, insert_event, get_metrics
from app.models import Event
from app.funnel import get_funnel
from app.anomalies import get_anomalies

app = FastAPI(
    title="Purplle Store Intelligence API",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    create_tables()


@app.get("/")
def home():
    return {
        "message": "Purplle Store Intelligence API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/metrics")
def metrics():
    return get_metrics()

@app.get("/funnel")
def funnel():
    return get_funnel()


@app.get("/anomalies")
def anomalies():
    return get_anomalies()

@app.post("/events/ingest")
def ingest_event(event: Event):

    insert_event(event)

    return {
        "message": "Event stored successfully"
    }