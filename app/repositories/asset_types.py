from app.models.db import get_db

def get_all_asset_types():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM asset_type")
    return [dict(row) for row in cur.fetchall()]

def create_asset_type(name: str):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO asset_type (name) VALUES (?)", (name,))
    db.commit()
    return cur.lastrowid
