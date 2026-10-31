# Query Plan Analysis – PostgreSQL

## 1. Introduction

This document explains how PostgreSQL executes SQL queries using `EXPLAIN` and `EXPLAIN ANALYZE`.

Query plans help us understand database performance and identify opportunities to optimize queries.

## 2. What is EXPLAIN?

`EXPLAIN` displays the execution plan PostgreSQL intends to use for a query.

It shows:
- Scan methods
- Estimated query cost
- Estimated number of rows
- Query execution strategy

Example:
EXPLAIN
SELECT *
FROM customers
WHERE email = 'chiranmayi@example.com';


## 3. What is EXPLAIN ANALYZE?

`EXPLAIN ANALYZE` actually executes the SQL query and displays its execution plan with measured performance information.

Example:

EXPLAIN ANALYZE
SELECT *
FROM products
WHERE price > 2000;


It provides:
- Actual execution time
- Actual number of rows
- Planning time
- Execution time
- Scan method

## 4. Sequential Scan

A sequential scan means PostgreSQL reads the table rows to find matching records.

Example:

Seq Scan on products


PostgreSQL may choose a sequential scan when:
- The table contains very few records.
- A large percentage of rows match the condition.
- Reading the whole table is cheaper than using an index.

## 5. Index Scan

An index scan uses an index to locate matching records without necessarily reading every table row.

Example query:
SELECT *
FROM customers
WHERE email = 'chiranmayi@example.com';


An index on the email column can help PostgreSQL find the matching customer efficiently, especially when the table becomes larger.

## 6. Observations from the Assignment

### Customer email search

Query:
EXPLAIN
SELECT *
FROM customers
WHERE email = 'chiranmayi@example.com';


Observation:

PostgreSQL selected a sequential scan even though an email index existed.

Reason:

The customers table contains only five records. Reading all five records can be cheaper than using an index.

### Product price search

Query:

EXPLAIN ANALYZE
SELECT *
FROM products
WHERE price > 2000;


Observation:

PostgreSQL selected a sequential scan and returned two matching products.

The measured execution time was approximately 0.030 milliseconds in the earlier assignment run.

Reason:

The products table contains only five records, so a sequential scan is reasonable.

## 7. Why Indexes Are Important

Indexes can improve:
- Searching records
- Filtering data
- Joining tables
- Sorting data in suitable queries

However, indexes also:
- Consume additional storage.
- Require maintenance during INSERT, UPDATE and DELETE operations.
- Can slow down write operations when too many unnecessary indexes exist.

## 8. Conclusion

Indexes are important for improving PostgreSQL query performance.

However, creating an index does not guarantee that PostgreSQL will use it.

The PostgreSQL query planner chooses the execution strategy based on estimated cost.

`EXPLAIN` and `EXPLAIN ANALYZE` help developers understand and optimize database queries.