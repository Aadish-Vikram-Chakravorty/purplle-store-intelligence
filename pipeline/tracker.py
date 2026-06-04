tracked_visitors = {}

def get_visitor_id(track_id):
    """
    Convert YOLO track IDs into stable visitor IDs.
    """

    if track_id not in tracked_visitors:
        tracked_visitors[track_id] = f"VIS_{track_id}"

    return tracked_visitors[track_id]