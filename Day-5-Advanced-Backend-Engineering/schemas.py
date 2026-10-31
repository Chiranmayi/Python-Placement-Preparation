
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


# Schema for creating a note
class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    body: str = Field(default="", max_length=10000)
    status: str = Field(default="draft")


# Schema for updating a note
class NoteUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=120)
    body: Optional[str] = Field(default=None, max_length=10000)
    status: Optional[str] = None


# Schema for sending note response
class NoteOut(BaseModel):
    id: int
    title: str
    body: str
    status: str

    # Allowing  Pydantic to read data from SQLAlchemy model objects
    model_config = ConfigDict(from_attributes=True)
