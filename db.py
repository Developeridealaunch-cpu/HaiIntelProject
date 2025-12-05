import sqlite3, json
from datetime import datetime

def init_db(path="results.db"):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id TEXT PRIMARY KEY,
        created_at TEXT,
        payload TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_result(path, data):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute(
        "INSERT OR REPLACE INTO results (id, created_at, payload) VALUES (?, ?, ?)",
        (data["id"], datetime.utcnow().isoformat(), json.dumps(data))
    )
    conn.commit()
    conn.close()
