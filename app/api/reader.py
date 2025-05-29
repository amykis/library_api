from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app.schemas.reader import ReaderCreate, ReaderResponse, ReaderUpdate
from app.crud import reader as crud_reader
from app.core.database import get_db

router = APIRouter()


@router.get("/", response_model=list[ReaderResponse])
def get_readers(db: Session = Depends(get_db)):
    return crud_reader.get_all_readers(db)


@router.post("/", response_model=ReaderResponse)
def create_reader(reader: ReaderCreate, db: Session = Depends(get_db)):
    return crud_reader.create_readers(db, reader)


@router.get('/by-email', response_model=ReaderResponse)
def get_reader_by_email(reader_email: str, db: Session = Depends(get_db)):
    reader = crud_reader.get_reader_by_email(db, reader_email)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return reader


@router.get('/{reader_id}', response_model=ReaderResponse)
def get_reader_by_id(reader_id: int, db: Session = Depends(get_db)):
    reader = crud_reader.get_reader_by_id(db, reader_id)
    if not reader:
        raise HTTPException(status_code=404, detail="Reader not found")
    return reader


@router.put("/{reader_id}", response_model=ReaderResponse)
def update_reader(reader_id: int, reader_data: ReaderUpdate, db: Session = Depends(get_db)):
    return crud_reader.update_reader(db, reader_id, reader_data)


@router.delete("/{reader_id}", response_model=ReaderResponse)
def delete_reader(reader_id: int, db: Session = Depends(get_db)):
    return crud_reader.delete_reader(db, reader_id)
