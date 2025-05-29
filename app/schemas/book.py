from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None
    isbn: Optional[str] = None
    copies: int = 1


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int

    model_config = {"from_attributes": True}


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    isbn: Optional[str] = None
    copies: Optional[int] = None
