from app.models.db import get_db

def get_all_assets():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        SELECT asset.*, customer.name AS customer_name, asset_type.name AS type_name
        FROM asset
        JOIN customer ON asset.customer_id = customer.id
        JOIN asset_type ON asset.asset_type_id = asset_type.id
    """)
    return [dict(row) for row in cur.fetchall()]

def get_asset_by_id(asset_id: int):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM asset WHERE id = ?", (asset_id,))
    row = cur.fetchone()
    return dict(row) if row else None

def create_asset(customer_id, name, asset_type_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO asset (customer_id, name, asset_type_id)
        VALUES (?, ?, ?)
    """, (customer_id, name, asset_type_id))
    db.commit()
    return cur.lastrowid
