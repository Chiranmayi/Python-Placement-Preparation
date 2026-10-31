# Test SQLAlchemy models

from app.database import Base
from app.models import Customer, Product, Order, OrderItem

print("SQLAlchemy models loaded successfully!")

print("\nTables registered in SQLAlchemy:")

for table_name in Base.metadata.tables:
    print(table_name)

print("\nTotal tables:", len(Base.metadata.tables))