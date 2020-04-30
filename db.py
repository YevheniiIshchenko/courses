import sqlite3

def get_db(request: str) -> list:
    try:
        conn = sqlite3.connect('./chinook.db')
        cur = conn.cursor()
        cur.execute(request)
        db = cur.fetchall()
        conn.close()
        return db
    finally:
        conn.close()