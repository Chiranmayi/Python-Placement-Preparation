from sqlalchemy import (
    BigInteger,
    String,
    Integer,
    Numeric,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    func
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


# 1. CUSTOMER MODEL
class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )

    full_name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150), unique=True, nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    orders: Mapped[list["Order"]] = relationship(
        back_populates="customer"
    )


# 2. PRODUCT MODEL
class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )

    product_name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    price: Mapped[float] = mapped_column(
        Numeric(12, 2), nullable=False
    )

    stock_quantity: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0"
    )

    order_items: Mapped[list["OrderItem"]] = relationship(
        back_populates="product"
    )


# 3. ORDER MODEL
class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )

    customer_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("customers.customer_id"),
        nullable=False
    )

    order_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    status: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default="NEW"
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="orders"
    )

    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order", cascade="all, delete-orphan"
    )


# 4. ORDER ITEM MODEL
class OrderItem(Base):
    __tablename__ = "order_items"

    __table_args__ = (
        UniqueConstraint(
            "order_id", "product_id",
            name="unique_order_product"
        ),
    )

    order_item_id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True
    )

    order_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("orders.order_id", ondelete="CASCADE"),
        nullable=False
    )

    product_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("products.product_id"),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer, nullable=False
    )

    unit_price: Mapped[float] = mapped_column(
        Numeric(12, 2), nullable=False
    )

    order: Mapped["Order"] = relationship(
        back_populates="items"
    )

    product: Mapped["Product"] = relationship(
        back_populates="order_items"
    )