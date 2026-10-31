
-- 1. SUBQUERY WITH WHERE
-- Find products whose price is greater than
-- the average price of all products

SELECT *
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);


-- 2. SUBQUERY WITH IN
-- Find customers who have placed orders

SELECT *
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
);


-- 3. SUBQUERY WITH NOT IN
-- Find customers who have not placed orders

SELECT *
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM orders
);


-- 4. EXISTS
-- Find customers who have at least one order

SELECT *
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);


-- 5. NOT EXISTS
-- Find customers who have no orders

SELECT *
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);


-- 6. COUNT
-- Count the number of orders for each customer

SELECT
    customer_id,
    COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id;


-- 7. SUM
-- Calculate total quantity of products sold

SELECT
    product_id,
    SUM(quantity) AS total_quantity_sold
FROM order_items
GROUP BY product_id;


-- 8. AVG
-- Calculate average product price

SELECT
    AVG(price) AS average_product_price
FROM products;


-- 9. GROUP BY WITH HAVING
-- Find customers who have placed more than one order

SELECT
    customer_id,
    COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- 10. GROUP BY WITH ORDER BY
-- Display customers and their total number of orders,
-- sorted from highest to lowest

SELECT
    customer_id,
    COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC;


-- 11. MULTIPLE AGGREGATE FUNCTIONS
-- Find total, minimum, maximum and average product prices

SELECT
    COUNT(*) AS total_products,
    SUM(price) AS total_price,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price,
    AVG(price) AS average_price
FROM products;


-- 12. CONDITIONAL AGGREGATION
-- Count orders based on their status

SELECT
    COUNT(*) AS total_orders,
    COUNT(*) FILTER (WHERE status = 'PAID') AS paid_orders,
    COUNT(*) FILTER (WHERE status = 'NEW') AS new_orders,
    COUNT(*) FILTER (WHERE status = 'SHIPPED') AS shipped_orders,
    COUNT(*) FILTER (WHERE status = 'CANCELLED') AS cancelled_orders
FROM orders;


-- 13. GROUP BY WITH CUSTOMER NAME
-- Display each customer's name and total orders

SELECT
    customers.full_name,
    COUNT(orders.order_id) AS total_orders
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.full_name
ORDER BY total_orders DESC;


-- 14. SUBQUERY IN SELECT
-- Display each product with the overall average price

SELECT
    product_name,
    price,
    (SELECT AVG(price) FROM products) AS average_price
FROM products;
