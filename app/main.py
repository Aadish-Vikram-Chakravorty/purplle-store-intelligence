from fastapi import FastAPI

app = FastAPI(
    title="Purplle Store Intelligence API",
    version="1.0.0"
)

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