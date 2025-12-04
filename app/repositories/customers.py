from app.models.db import get_db

def get_all_customers():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM customer")
    return [dict(row) for row in cur.fetchall()]

def get_customer_by_id(customer_id: int):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM customer WHERE id = ?", (customer_id,))
    row = cur.fetchone()
    return dict(row) if row else None

def create_customer(name: str):
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO customer (name) VALUES (?)", (name,))
    db.commit()
    return cur.lastrowid

def delete_customer(customer_id: int):
    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM customer WHERE id = ?", (customer_id,))
    db.commit()
