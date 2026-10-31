-- 1. BASIC CTE
-- Find products whose price is greater than 2000

WITH expensive_products AS (
    SELECT *
    FROM products
    WHERE price > 2000
)
SELECT *
FROM expensive_products;


-- 2. CTE WITH AGGREGATE FUNCTION
-- Calculate total orders for each customer

WITH customer_orders AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY customer_id
)
SELECT *
FROM customer_orders;


-- 3. CTE WITH JOIN
-- Display customer names and their order counts

WITH customer_orders AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY customer_id
)
SELECT
    customers.full_name,
    COALESCE(customer_orders.total_orders, 0) AS total_orders
FROM customers
LEFT JOIN customer_orders
ON customers.customer_id = customer_orders.customer_id;


-- 4. MULTIPLE CTEs
-- Calculate total sales for each order

WITH order_totals AS (
    SELECT
        order_id,
        SUM(quantity * unit_price) AS total_amount
    FROM order_items
    GROUP BY order_id
),
paid_orders AS (
    SELECT order_id, total_amount
    FROM order_totals
    WHERE total_amount > 10000
)
SELECT *
FROM paid_orders;


-- 5. ROW_NUMBER()
-- Assign a unique row number to each product
-- based on price (highest first)

SELECT
    product_name,
    price,
    ROW_NUMBER() OVER (ORDER BY price DESC) AS row_number
FROM products;


-- 6. RANK()
-- Rank products based on price

SELECT
    product_name,
    price,
    RANK() OVER (ORDER BY price DESC) AS product_rank
FROM products;


-- 7. DENSE_RANK()
-- Rank products without skipping rank numbers

SELECT
    product_name,
    price,
    DENSE_RANK() OVER (ORDER BY price DESC) AS dense_rank
FROM products;


-- 8. PARTITION BY
-- Number each order separately for each customer

SELECT
    customer_id,
    order_id,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY order_id
    ) AS customer_order_number
FROM orders;


-- 9. SUM() WINDOW FUNCTION
-- Show each order item and the running total quantity

SELECT
    order_id,
    product_id,
    quantity,
    SUM(quantity) OVER (
        ORDER BY order_id, order_item_id
    ) AS running_quantity
FROM order_items;


-- 10. LAG()
-- Compare each product price with the previous product price

SELECT
    product_name,
    price,
    LAG(price) OVER (ORDER BY price DESC) AS previous_price
FROM products;


-- 11. LEAD()
-- Display the next product price

SELECT
    product_name,
    price,
    LEAD(price) OVER (ORDER BY price DESC) AS next_price
FROM products;


-- 12. CUSTOMER ORDER RANKING
-- Rank customers based on their number of orders

SELECT
    customer_id,
    COUNT(*) AS total_orders,
    RANK() OVER (
        ORDER BY COUNT(*) DESC
    ) AS customer_rank
FROM orders
GROUP BY customer_id;


-- 13. RECURSIVE CTE
-- Generate numbers from 1 to 5

WITH RECURSIVE number_series AS (
    SELECT 1 AS number

    UNION ALL

    SELECT number + 1
    FROM number_series
    WHERE number < 5
)
SELECT *
FROM number_series;
