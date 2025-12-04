-- =========================================================
-- ROLE
-- =========================================================
CREATE TABLE role (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- =========================================================
-- EMPLOYEE
-- =========================================================
CREATE TABLE employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    login TEXT NOT NULL UNIQUE,
    role_id INTEGER NOT NULL,
    last_login DATETIME,
    password_hash TEXT NOT NULL,
    FOREIGN KEY (role_id) REFERENCES role(id)
);

-- =========================================================
-- CUSTOMER
-- =========================================================
CREATE TABLE customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- =========================================================
-- ASSET_TYPE
-- =========================================================
CREATE TABLE asset_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- =========================================================
-- ASSET
-- =========================================================
CREATE TABLE asset (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    asset_type_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (asset_type_id) REFERENCES asset_type(id)
);

-- =========================================================
-- ACCESS_TYPE
-- =========================================================
CREATE TABLE access_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- =========================================================
-- ACCESS_REQUEST
-- =========================================================
CREATE TABLE access_request (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    asset_id INTEGER NOT NULL,
    status TEXT NOT NULL,                        -- pending/approved/rejected
    access_type_id INTEGER NOT NULL,
    created_at DATETIME NOT NULL,
    approved_at DATETIME,
    approved_by INTEGER,
    reason TEXT,
    FOREIGN KEY (employee_id) REFERENCES employee(id),
    FOREIGN KEY (asset_id) REFERENCES asset(id),
    FOREIGN KEY (access_type_id) REFERENCES access_type(id),
    FOREIGN KEY (approved_by) REFERENCES employee(id)
);

-- =========================================================
-- ACCESS
-- =========================================================
CREATE TABLE access (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    asset_id INTEGER NOT NULL,
    status TEXT NOT NULL,                        -- active/revoked/expired
    approved_by INTEGER NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employee(id),
    FOREIGN KEY (asset_id) REFERENCES asset(id),
    FOREIGN KEY (approved_by) REFERENCES employee(id)
);
