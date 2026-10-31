
from sqlalchemy import Column, Integer, String, Text
from database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    body = Column(Text, default="")
    status = Column(String(20), default="draft")
