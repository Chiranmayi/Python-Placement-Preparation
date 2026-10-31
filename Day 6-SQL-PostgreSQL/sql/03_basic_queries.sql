-- DAY 6: BASIC SQL QUERIES

-- 1. SELECT ALL CUSTOMERS
SELECT * FROM customers;


-- 2. SELECT SPECIFIC COLUMNS
SELECT full_name, email
FROM customers;


-- 3. WHERE CONDITION
-- Find customers whose name is Chiranmayi
SELECT *
FROM customers
WHERE full_name = 'Chiranmayi';


-- 4. COMPARISON OPERATORS
-- Find products costing more than 2000
SELECT *
FROM products
WHERE price > 2000;


-- 5. AND OPERATOR
-- Products costing more than 1000 and stock greater than 10
SELECT *
FROM products
WHERE price > 1000 AND stock_quantity > 10;


-- 6. OR OPERATOR
-- Products costing less than 1000 or stock greater than 20
SELECT *
FROM products
WHERE price < 1000 OR stock_quantity > 20;


-- 7. DISTINCT
-- Display unique order statuses
SELECT DISTINCT status
FROM orders;


-- 8. LIKE
-- Find customers whose names start with A
SELECT *
FROM customers
WHERE full_name LIKE 'A%';


-- 9. ILIKE
-- Case-insensitive search
SELECT *
FROM customers
WHERE full_name ILIKE 'a%';


-- 10. IS NULL
-- Find orders where status is NULL
SELECT *
FROM orders
WHERE status IS NULL;


-- 11. ORDER BY ASCENDING
-- Sort products from lowest to highest price
SELECT *
FROM products
ORDER BY price ASC;


-- 12. ORDER BY DESCENDING
-- Sort products from highest to lowest price
SELECT *
FROM products
ORDER BY price DESC;


-- 13. LIMIT
-- Display only the first 3 products
SELECT *
FROM products
LIMIT 3;


-- 14. OFFSET
-- Skip the first 2 products
SELECT *
FROM products
OFFSET 2;


-- 15. LIMIT AND OFFSET
-- Display 2 products after skipping the first 2
SELECT *
FROM products
LIMIT 2 OFFSET 2;


-- 16. BETWEEN
-- Find products priced between 1000 and 30000
SELECT *
FROM products
WHERE price BETWEEN 1000 AND 30000;


-- 17. IN
-- Find orders with PAID or NEW status
SELECT *
FROM orders
WHERE status IN ('PAID', 'NEW');


-- 18. NOT IN
-- Find orders that are not PAID or NEW
SELECT *
FROM orders
WHERE status NOT IN ('PAID', 'NEW');


-- 19. COUNT
-- Count total customers
SELECT COUNT(*) AS total_customers
FROM customers;


-- 20. MIN, MAX, AVG
-- Find minimum, maximum and average product price
SELECT
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price,
    AVG(price) AS average_price
FROM products;