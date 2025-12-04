-- =========================================================
-- ROLE
-- =========================================================
INSERT INTO role (name) VALUES
    ('admin'),
    ('technician'),
    ('auditor');

-- =========================================================
-- EMPLOYEE
-- =========================================================
INSERT INTO employee (first_name, last_name, login, role_id, last_login, password_hash)
VALUES
    ('Karel', 'Novak', 'k.novak', 1, '2025-01-04 10:15', 'hash_admin123'),
    ('Petr', 'Svoboda', 'p.svoboda', 2, '2025-01-06 13:45', 'hash_tech456'),
    ('Lucie', 'Kralova', 'l.kralova', 3, NULL, 'hash_auditor789');

-- =========================================================
-- CUSTOMER
-- =========================================================
INSERT INTO customer (name) VALUES
    ('Skoda Auto'),
    ('CEZ Group'),
    ('O2 Czech Republic');

-- =========================================================
-- ASSET_TYPE
-- =========================================================
INSERT INTO asset_type (name) VALUES
    ('Active Directory'),
    ('Firewall'),
    ('VPN Gateway'),
    ('Database'),
    ('Switch');

-- =========================================================
-- ASSET
-- =========================================================
INSERT INTO asset (customer_id, name, asset_type_id) VALUES
    (1, 'AD-Primary', 1),    -- Skoda Auto
    (1, 'FW-PaloAlto-1', 2),
    (2, 'CEZ-VPN01', 3),     -- CEZ Group
    (3, 'CRM-Database', 4);  -- O2

-- =========================================================
-- ACCESS_TYPE
-- =========================================================
INSERT INTO access_type (name) VALUES
    ('read-only'),
    ('read-write'),
    ('admin'),
    ('maintenance');

-- =========================================================
-- ACCESS_REQUEST
-- =========================================================
INSERT INTO access_request
(employee_id, asset_id, status, access_type_id, created_at, approved_at, approved_by, reason)
VALUES
    (2, 1, 'pending', 2, '2025-02-01 09:30', NULL, NULL, 'Need access for maintenance'),
    (2, 2, 'approved', 1, '2025-02-02 10:00', '2025-02-02 11:00', 1, 'Firewall checkup'),
    (3, 1, 'rejected', 1, '2025-02-03 08:15', NULL, 1, 'Not authorized');

-- =========================================================
-- ACCESS
-- =========================================================
INSERT INTO access (employee_id, asset_id, status, approved_by)
VALUES
    (2, 2, 'active', 1),
    (3, 1, 'revoked', 1);
