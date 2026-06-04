from app.database import get_connection


def get_anomalies():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM events WHERE event_type='ENTRY'"
    )
    entries = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM events WHERE event_type='EXIT'"
    )
    exits = cursor.fetchone()[0]

    conn.close()

    anomalies = []

    if entries > exits + 10:
        anomalies.append({
            "type": "QUEUE_BUILDUP",
            "message": "Possible crowd build-up detected"
        })

    if entries == 0:
        anomalies.append({
            "type": "NO_ACTIVITY",
            "message": "No visitor activity detected"
        })

    if exits == 0 and entries > 0:
        anomalies.append({
            "type": "LOW_CONVERSION",
            "message": "Visitors entered but no exits recorded"
        })

    return {
        "anomalies": anomalies
    }
    