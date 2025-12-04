from app.models.db import get_db

def get_all_employees():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM employee")
    return [dict(row) for row in cur.fetchall()]

def get_employee_by_id(employee_id: int):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM employee WHERE id = ?", (employee_id,))
    row = cur.fetchone()
    return dict(row) if row else None

def get_employee_by_login(login: str):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM employee WHERE login = ?", (login,))
    row = cur.fetchone()
    return dict(row) if row else None

def create_employee(first_name, last_name, login, role_id, password_hash):
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO employee (first_name, last_name, login, role_id, password_hash)
        VALUES (?, ?, ?, ?, ?)
    """, (first_name, last_name, login, role_id, password_hash))
    db.commit()
    return cur.lastrowid

def delete_employee(employee_id: int):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM employee WHERE id = ?", (employee_id,))
    db.commit()
