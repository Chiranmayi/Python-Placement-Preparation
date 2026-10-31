from fastapi import APIRouter, Depends
from dependencies import common_pagination

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Mobile", "price": 25000},
    {"id": 3, "name": "Headphones", "price": 2000}
]


@router.get("/")
def get_products(paging: dict = Depends(common_pagination)):

    start = paging["skip"]
    end = start + paging["limit"]

    return {
        "products": products[start:end],
        "skip": paging["skip"],
        "limit": paging["limit"]
    }


@router.get("/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}