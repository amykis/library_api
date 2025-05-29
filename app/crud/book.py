from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate


def get_all_books(db: Session):
    return db.query(Book).all()


def create_book(db: Session, book: BookCreate):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db: Session, book_id: int, book_data):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None
    for key, value in book_data.dict(exclude_unset=True).items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book
