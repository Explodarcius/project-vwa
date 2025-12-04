from app.models.db import get_db

def get_all_accesses():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        SELECT ac.*, e.first_name || ' ' || e.last_name AS employee_name,
               a.name AS asset_name
        FROM access ac
        JOIN employee e ON ac.employee_id = e.id
        JOIN asset a ON ac.asset_id = a.id
    """)
    return [dict(row) for row in cur.fetchall()]

def create_access(employee_id, asset_id, approved_by):
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO access (employee_id, asset_id, status, approved_by)
        VALUES (?, ?, 'active', ?)
    """, (employee_id, asset_id, approved_by))
    db.commit()
    return cur.lastrowid
