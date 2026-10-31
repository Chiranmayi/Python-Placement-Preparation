# Day 6 – SQL and PostgreSQL

## Project Overview

This project covers SQL and PostgreSQL concepts, database design, SQLAlchemy ORM, Alembic migrations, and query performance optimization.

The project demonstrates how to create relational database tables, perform SQL operations, connect Python applications to PostgreSQL, and manage database relationships.

## Technologies Used

- Python
- PostgreSQL 18.6
- SQLAlchemy 2.x
- Alembic
- Psycopg
- Asyncpg
- Git and GitHub

## Project Structure

Day 6-SQL-PostgreSQL/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   └── models.py
│
├── migrations/
│   ├── versions/
│   └── env.py
│
├── sql/
│   ├── 01_create_tables.sql
│   ├── 02_insert_data.sql
│   ├── 03_basic_queries.sql
│   ├── 04_joins.sql
│   ├── 05_subqueries_aggregates.sql
│   ├── 06_ctes_window_functions.sql
│   ├── 07_transactions.sql
│   └── 08_indexes_performance.sql
│
├── outputs/
│   └── query_plan.md
│
├── test_connection.py
├── test_models.py
├── test_relationships.py
├── test_eager_loading.py
├── alembic.ini
├── requirements.txt
└── README.md

## Database Setup

### 1. Install PostgreSQL

Install PostgreSQL and ensure the database server is running.

### 2. Create the Database

Open the PostgreSQL terminal (`psql`) and execute:


CREATE DATABASE day6_assignment;

Connect to the database:

\c day6_assignment


### 3. Execute SQL Scripts

Run the SQL files in the following order:

1. `01_create_tables.sql`
2. `02_insert_data.sql`
3. `03_basic_queries.sql`
4. `04_joins.sql`
5. `05_subqueries_aggregates.sql`
6. `06_ctes_window_functions.sql`
7. `07_transactions.sql`
8. `08_indexes_performance.sql`

Example:


\i 'C:/path/to/Day 6-SQL-PostgreSQL/sql/01_create_tables.sql'


Replace the path with the actual location of your project.

## Python Environment Setup

Open the project folder in VS Code.

Create and activate a virtual environment if you do not already have one:

python -m venv .venv


Activate it:

.venv\Scripts\Activate.ps1


Install dependencies:


python -m pip install -r requirements.txt


## Database Connection

The application uses SQLAlchemy to connect Python with PostgreSQL.

Set the database URL as an environment variable in PowerShell:


$env:DATABASE_URL="postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/day6_assignment"


Replace `YOUR_PASSWORD` with your PostgreSQL password.

Do not commit passwords or other database credentials to GitHub.

## SQLAlchemy Models

The application contains four database models:

- Customer
- Product
- Order
- OrderItem

These models represent the corresponding PostgreSQL tables and define their relationships using SQLAlchemy ORM.

## Alembic Migrations

Alembic is used to manage database schema versions.

Initialize Alembic:

alembic init migrations


Generate a migration:


alembic revision --autogenerate -m "create database models"


Apply the migration:


alembic upgrade head


Check the current migration:

alembic current


The initial migration in this project is a baseline because the database tables were created using SQL scripts before Alembic was configured.

## Testing

Run the following Python files from the Day 6 project directory:

### Test database connection


python test_connection.py


### Test SQLAlchemy models


python test_models.py


### Test SQLAlchemy relationships


python test_relationships.py


### Test eager loading


python test_eager_loading.py


## Query Performance

The project demonstrates:

- Database indexes
- Sequential scans
- Index scans
- EXPLAIN
- EXPLAIN ANALYZE
- Query execution plans
- N+1 query problem
- Eager loading using selectinload()

Refer to `outputs/query_plan.md` for the query performance analysis.

## Concepts Covered

- Relational database design
- Primary keys and foreign keys
- Database constraints
- Normalization
- SQL CRUD operations
- Joins and subqueries
- Aggregate functions
- Common Table Expressions (CTEs)
- Window functions
- Transactions and ACID properties
- Indexing and query optimization
- SQLAlchemy ORM
- Database relationships
- Alembic migrations
- Eager loading and N+1 query optimization

## Conclusion

This project provides practical experience with PostgreSQL, SQL, SQLAlchemy ORM, database relationships, migrations, and query performance optimization using Python.