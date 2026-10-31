
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# 1. DATABASE URL
# Read the connection URL securely from environment variables

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not set. "
        "Please configure your PostgreSQL connection URL."
    )


# 2. CREATE DATABASE ENGINE

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=True
)


# 3. CREATE DATABASE SESSION

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# 4. CREATE BASE CLASS

class Base(DeclarativeBase):
    pass


# 5. DATABASE DEPENDENCY

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
