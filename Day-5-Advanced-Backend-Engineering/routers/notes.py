
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

from database import get_db
from models import Note
from schemas import NoteCreate, NoteUpdate, NoteOut
from security import verify_api_key
from rate_limiter import rate_limit


router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
    dependencies=[
        Depends(verify_api_key),
        Depends(rate_limit)
    ]
)


# CREATE NOTE
@router.post(
    "/",
    response_model=NoteOut,
    status_code=status.HTTP_201_CREATED
)
def create_note(
    note_data: NoteCreate,
    db: Session = Depends(get_db)
):
    new_note = Note(
        title=note_data.title,
        body=note_data.body,
        status=note_data.status
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


# GET ALL NOTES WITH SEARCH AND PAGINATION
@router.get("/")
def get_notes(
    search: str = "",
    note_status: str = "",
    limit: int = 10,
    offset: int = 0,
    sort_by: str = "id",
    order: str = "asc",
    db: Session = Depends(get_db)
):
    if limit < 1 or limit > 100:
        raise HTTPException(
            status_code=422,
            detail="Limit must be between 1 and 100"
        )

    if offset < 0:
        raise HTTPException(
            status_code=422,
            detail="Offset cannot be negative"
        )

    allowed_sort_fields = {
        "id": Note.id,
        "title": Note.title,
        "status": Note.status
    }

    if sort_by not in allowed_sort_fields:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort field"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be asc or desc"
        )

    query = db.query(Note)

    if search:
        query = query.filter(
            Note.title.ilike(f"%{search}%")
        )

    if note_status:
        query = query.filter(
            Note.status == note_status
        )

    sort_column = allowed_sort_fields[sort_by]

    if order == "desc":
        query = query.order_by(sort_column.desc())
    else:
        query = query.order_by(sort_column.asc())

    total = query.count()

    notes = query.offset(offset).limit(limit).all()

    return {
        "items": notes,
        "total": total,
        "limit": limit,
        "offset": offset
    }


# GET ONE NOTE
@router.get("/{note_id}", response_model=NoteOut)
def get_note(
    note_id: int,
    db: Session = Depends(get_db)
):
    note = db.query(Note).filter(
        Note.id == note_id
    ).first()

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note


# UPDATE NOTE
@router.patch("/{note_id}", response_model=NoteOut)
def update_note(
    note_id: int,
    note_data: NoteUpdate,
    db: Session = Depends(get_db)
):
    note = db.query(Note).filter(
        Note.id == note_id
    ).first()

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    update_data = note_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(note, field, value)

    db.commit()
    db.refresh(note)

    return note


# DELETE NOTE
@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db)
):
    note = db.query(Note).filter(
        Note.id == note_id
    ).first()

    if not note:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    db.delete(note)
    db.commit()

    return None
