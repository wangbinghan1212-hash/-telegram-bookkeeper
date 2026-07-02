import sqlite3
from config import DATABASE

def connect():
    return sqlite3.connect(DATABASE)

def init_db():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id INTEGER,
        user_name TEXT,
        amount REAL,
        rate REAL,
        exchange REAL,
        type TEXT,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()