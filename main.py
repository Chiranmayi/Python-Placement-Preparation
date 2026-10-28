
from fastapi import FastAPI, HTTPException, Query, File, UploadFile
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Day 3 Items API")

class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Item name must not be blank")

        return value


# Task D: Define the public response structure
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float


# Temporary storage for practice (data resets on restart)
items: dict[int, ItemResponse] = {}
next_id = 1


@app.get("/")
def home():
    return {"message": "Day 3 Items API is running"}


# Task B: Get one item by its ID
# Task D: Return 404 when the item does not exist
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    item = items.get(item_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item


# Task B: Get a list of items with a limit
@app.get("/items", response_model=list[ItemResponse])
def get_items(
    limit: int = Query(default=10, ge=1, le=100)
):
    return list(items.values())[:limit]


# Task B and C: Create an item with validated input
# Task D: Return 201 Created and a defined response model
@app.post(
    "/items",
    response_model=ItemResponse,
    status_code=201
)
def create_item(item: ItemCreate):
    global next_id

    new_item = ItemResponse(
        id=next_id,
        name=item.name,
        price=item.price
    )

    items[next_id] = new_item
    next_id += 1

    return new_item


# Task E: Basic file upload endpoint
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File metadata received"
    }
