from app.models.db import get_db

def get_all_roles():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM role")
    return [dict(row) for row in cur.fetchall()]

def get_role_by_id(role_id: int):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM role WHERE id = ?", (role_id,))
    return dict(cur.fetchone()) if cur.fetchone() else None

def create_role(name: str):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO role (name) VALUES (?)", (name,))
    db.commit()
    return cur.lastrowid

def delete_role(role_id: int):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM role WHERE id = ?", (role_id,))
    db.commit()
