from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookResponse, BookUpdate
from app.crud import book as crud_book
from app.core.database import get_db

router = APIRouter()


@router.get("/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return crud_book.get_all_books(db)


@router.get("/{book_id}", response_model=BookResponse)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = crud_book.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return crud_book.create_book(db, book)


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    return crud_book.update_book(db, book_id, book_data)


@router.delete("/{book_id}", response_model=BookResponse)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud_book.delete_book(db, book_id)
