from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database import SessionLocal
from app.models import Customer, Order


# Create database session
db = SessionLocal()

try:
    # Retrieve customers and their related orders and items
    statement = (
        select(Customer)
        .options(
            selectinload(Customer.orders)
            .selectinload(Order.items)
        )
    )

    # Execute query and retrieve customers
    customers = db.scalars(statement).all()

    print("\nCUSTOMERS AND THEIR ORDERS")
    print("--------------------------")

    for customer in customers:

        print(f"\nCustomer: {customer.full_name}")
        print(f"Email: {customer.email}")

        for order in customer.orders:

            print(
                f"Order ID: {order.order_id}, "
                f"Status: {order.status}"
            )

            for item in order.items:

                print(
                    f"Product ID: {item.product_id}, "
                    f"Quantity: {item.quantity}"
                )

finally:
    # Close database session
    db.close()
