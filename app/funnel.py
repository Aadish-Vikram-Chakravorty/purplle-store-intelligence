from app.database import get_connection

def get_funnel():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(DISTINCT visitor_id) FROM events WHERE event_type='ENTRY'"
    )
    visitors = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(DISTINCT visitor_id) FROM events WHERE event_type='EXIT'"
    )
    completed = cursor.fetchone()[0]

    drop_off = visitors - completed

    conn.close()

    return {
        "visitors": visitors,
        "completed": completed,
        "drop_off": drop_off,
        "conversion_rate": round(
        (completed / visitors * 100),
        2
    ) if visitors > 0 else 0
 }