-- 1. BASIC TRANSACTION
-- Start a transaction, update product stock,
-- and save the changes

BEGIN;

UPDATE products
SET stock_quantity = stock_quantity - 1
WHERE product_id = 1;

COMMIT;


-- 2. ROLLBACK
-- Make a temporary change and undo it

BEGIN;

UPDATE products
SET stock_quantity = stock_quantity - 5
WHERE product_id = 2;

ROLLBACK;


-- 3. TRANSACTION WITH MULTIPLE OPERATIONS
-- Reduce stock and create an order item together

BEGIN;

UPDATE products
SET stock_quantity = stock_quantity - 1
WHERE product_id = 3
AND stock_quantity >= 1;

INSERT INTO order_items
(order_id, product_id, quantity, unit_price)
SELECT
    1,
    product_id,
    1,
    price
FROM products
WHERE product_id = 3
AND stock_quantity >= 0;

COMMIT;


-- 4. SAVEPOINT
-- Save a point inside a transaction

BEGIN;

UPDATE products
SET stock_quantity = stock_quantity - 1
WHERE product_id = 4;

SAVEPOINT stock_updated;

UPDATE products
SET price = price + 500
WHERE product_id = 4;

ROLLBACK TO SAVEPOINT stock_updated;

COMMIT;


-- 5. CHECK PRODUCT STOCK
-- Display current product stock

SELECT
    product_id,
    product_name,
    stock_quantity
FROM products
ORDER BY product_id;


-- 6. CHECK PRODUCT PRICES
-- Display current product prices

SELECT
    product_id,
    product_name,
    price
FROM products
ORDER BY product_id;


-- 7. TRANSACTION WITH VALIDATION
-- Update stock only when enough stock is available

BEGIN;

UPDATE products
SET stock_quantity = stock_quantity - 2
WHERE product_id = 5
AND stock_quantity >= 2;

COMMIT;
