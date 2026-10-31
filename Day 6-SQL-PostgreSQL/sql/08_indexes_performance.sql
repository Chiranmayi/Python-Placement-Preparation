

-- 1. CREATE INDEX ON CUSTOMER EMAIL
-- Helps PostgreSQL search customers by email

CREATE INDEX idx_customers_email
ON customers(email);


-- 2. CREATE INDEX ON PRODUCT NAME
-- Helps search products by name

CREATE INDEX idx_products_name
ON products(product_name);


-- 3. CREATE INDEX ON ORDER CUSTOMER ID
-- Helps find orders belonging to a customer

CREATE INDEX idx_orders_customer_id
ON orders(customer_id);


-- 4. CREATE INDEX ON ORDER DATE
-- Helps filter and sort orders by date

CREATE INDEX idx_orders_order_date
ON orders(order_date);


-- 5. COMPOSITE INDEX
-- Index using two columns together

CREATE INDEX idx_order_items_order_product
ON order_items(order_id, product_id);


-- 6. UNIQUE INDEX
-- Ensures customer email values remain unique

CREATE UNIQUE INDEX idx_customers_email_unique
ON customers(email);


-- 7. CHECK EXISTING INDEXES
-- Display indexes available on customers

SELECT *
FROM pg_indexes
WHERE tablename = 'customers';


-- 8. EXPLAIN
-- Display the query execution plan

EXPLAIN
SELECT *
FROM customers
WHERE email = 'chiranmayi@example.com';


-- 9. EXPLAIN ANALYZE
-- Execute the query and show actual performance details

EXPLAIN ANALYZE
SELECT *
FROM products
WHERE price > 2000;


-- 10. QUERY USING INDEXED COLUMN
-- Search for a customer using email

SELECT *
FROM customers
WHERE email = 'chiranmayi@example.com';


-- 11. QUERY USING MULTIPLE CONDITIONS
-- Search orders for a customer and order date

SELECT *
FROM orders
WHERE customer_id = 1
AND order_date >= CURRENT_DATE;


-- 12. DISPLAY ALL INDEXES
-- View indexes in the current database schema

SELECT
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;
