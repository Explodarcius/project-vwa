from app.models.db import get_db

def get_all_requests():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        SELECT ar.*, e.first_name || ' ' || e.last_name AS employee_name,
               a.name AS asset_name, at.name AS access_type_name
        FROM access_request ar
        JOIN employee e ON ar.employee_id = e.id
        JOIN asset a ON ar.asset_id = a.id
        JOIN access_type at ON ar.access_type_id = at.id
    """)
    return [dict(row) for row in cur.fetchall()]

def get_request_by_id(request_id: int):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM access_request WHERE id = ?", (request_id,))
    row = cur.fetchone()
    return dict(row) if row else None

def create_request(employee_id, asset_id, access_type_id, reason):
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO access_request (employee_id, asset_id, access_type_id, status, created_at, reason)
        VALUES (?, ?, ?, 'pending', datetime('now'), ?)
    """, (employee_id, asset_id, access_type_id, reason))
    db.commit()
    return cur.lastrowid

def update_request_status(request_id, status, approved_by=None):
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        UPDATE access_request
        SET status = ?, approved_by = ?, approved_at = datetime('now')
        WHERE id = ?
    """, (status, approved_by, request_id))
    db.commit()
