import sqlite3

DB_NAME = "data/events.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        visitor_id TEXT,
        camera_id TEXT,
        event_type TEXT,
        zone TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

import sqlite3

DB_NAME = "data/events.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        visitor_id TEXT,
        camera_id TEXT,
        event_type TEXT,
        zone TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_event(event):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO events
    (visitor_id, camera_id, event_type, zone, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """, (
        event.visitor_id,
        event.camera_id,
        event.event_type,
        event.zone,
        event.timestamp
    ))

    conn.commit()
    conn.close()

def get_metrics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM events")
    total_events = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM events WHERE event_type = 'ENTRY'"
    )
    entries = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM events WHERE event_type = 'EXIT'"
    )
    exits = cursor.fetchone()[0]

    conn.close()

    return {
        "total_events": total_events,
        "entries": entries,
        "exits": exits
    }