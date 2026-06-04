from datetime import datetime

def create_event(
    visitor_id,
    camera_id,
    event_type,
    zone
):
    return {
        "visitor_id": visitor_id,
        "camera_id": camera_id,
        "event_type": event_type,
        "zone": zone,
        "timestamp": str(datetime.now())
    }