from app.models.db import get_db

def get_all_access_types():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM access_type")
    return [dict(row) for row in cur.fetchall()]

def create_access_type(name: str):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO access_type (name) VALUES (?)", (name,))
    db.commit()
    return cur.lastrowid
