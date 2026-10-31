
-- =========================================
-- DAY 6: INSERT SAMPLE DATA
-- =========================================


-- 1. INSERT CUSTOMERS
INSERT INTO customers (full_name, email)
VALUES
    ('Chiranmayi', 'chiranmayi@example.com'),
    ('Asha Rao', 'asha@example.com'),
    ('Rahul Kumar', 'rahul@example.com'),
    ('Priya Sharma', 'priya@example.com'),
    ('Arjun Reddy', 'arjun@example.com');


-- 2. INSERT PRODUCTS
INSERT INTO products (product_name, price, stock_quantity)
VALUES
    ('Laptop', 55000.00, 10),
    ('Mobile', 25000.00, 20),
    ('Headphones', 2000.00, 30),
    ('Keyboard', 1500.00, 15),
    ('Mouse', 800.00, 25);


-- 3. INSERT ORDERS
INSERT INTO orders (customer_id, status)
VALUES
    (1, 'PAID'),
    (1, 'NEW'),
    (2, 'PAID'),
    (3, 'SHIPPED'),
    (4, 'CANCELLED');


-- 4. INSERT ORDER ITEMS
INSERT INTO order_items
    (order_id, product_id, quantity, unit_price)
VALUES
    (1, 1, 1, 55000.00),
    (1, 3, 2, 2000.00),
    (2, 2, 1, 25000.00),
    (3, 4, 2, 1500.00),
    (3, 5, 1, 800.00),
    (4, 1, 1, 55000.00),
    (5, 3, 1, 2000.00);


-- 5. VERIFY INSERTED DATA
SELECT COUNT(*) AS total_customers FROM customers;
SELECT COUNT(*) AS total_products FROM products;
SELECT COUNT(*) AS total_orders FROM orders;
SELECT COUNT(*) AS total_order_items FROM order_items;
