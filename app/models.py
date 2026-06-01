from pydantic import BaseModel


class Event(BaseModel):
    visitor_id: str
    camera_id: str
    event_type: str
    zone: str
    timestamp: str