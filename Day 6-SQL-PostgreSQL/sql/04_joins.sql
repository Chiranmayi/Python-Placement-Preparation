
-- =========================================
-- DAY 6: SQL JOINS
-- =========================================


-- 1. INNER JOIN
-- Display customers who have placed orders

SELECT
    customers.customer_id,
    customers.full_name,
    orders.order_id,
    orders.status
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;


-- 2. LEFT JOIN
-- Display all customers, including customers
-- who have not placed any orders

SELECT
    customers.customer_id,
    customers.full_name,
    orders.order_id,
    orders.status
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;


-- 3. RIGHT JOIN
-- Display all orders and their customer details

SELECT
    customers.full_name,
    orders.order_id,
    orders.status
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id;


-- 4. FULL OUTER JOIN
-- Display all customers and all orders,
-- whether they match or not

SELECT
    customers.full_name,
    orders.order_id,
    orders.status
FROM customers
FULL OUTER JOIN orders
ON customers.customer_id = orders.customer_id;


-- 5. CROSS JOIN
-- Combine every customer with every product

SELECT
    customers.full_name,
    products.product_name
FROM customers
CROSS JOIN products;


-- 6. SELF JOIN
-- Compare customers with other customers
-- using the same table

SELECT
    c1.full_name AS customer_one,
    c2.full_name AS customer_two
FROM customers c1
JOIN customers c2
ON c1.customer_id < c2.customer_id;


-- 7. JOIN THREE TABLES
-- Display customer names, order IDs and product names

SELECT
    customers.full_name,
    orders.order_id,
    products.product_name,
    order_items.quantity,
    order_items.unit_price
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
INNER JOIN order_items
ON orders.order_id = order_items.order_id
INNER JOIN products
ON order_items.product_id = products.product_id;


-- 8. LEFT JOIN WITH WHERE
-- Find customers who have not placed any orders

SELECT
    customers.customer_id,
    customers.full_name
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id
WHERE orders.order_id IS NULL;


-- 9. ORDER TOTAL
-- Calculate the total amount of each order

SELECT
    orders.order_id,
    customers.full_name,
    SUM(order_items.quantity * order_items.unit_price) AS order_total
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id
INNER JOIN order_items
ON orders.order_id = order_items.order_id
GROUP BY orders.order_id, customers.full_name
ORDER BY orders.order_id;
