from app.database import SessionLocal
from app.models import Customer, Order


# Create database session
db = SessionLocal()

try:
    # Get all customers
    customers = db.query(Customer).all()

    print("\nCUSTOMER AND ORDER DETAILS")
    print("--------------------------")

    for customer in customers:

        print(f"\nCustomer: {customer.full_name}")
        print(f"Email: {customer.email}")

        # Access related orders using relationship
        for order in customer.orders:
            print(
                f"Order ID: {order.order_id}, "
                f"Status: {order.status}"
            )

            # Access order items
            for item in order.items:
                print(
                    f"  Product: {item.product.product_name}, "
                    f"Quantity: {item.quantity}"
                )

finally:
    # Close database session
    db.close()