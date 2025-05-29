from sqlalchemy.orm import Session
from app.models.reader import Reader
from app.schemas.reader import ReaderCreate
from app.core.security import hash_password


def get_all_readers(db: Session):
    return db.query(Reader).all()


def create_readers(db: Session, reader: ReaderCreate):
    new_reader = Reader(name=reader.name, email=reader.email)
    db.add(new_reader)
    db.commit()
    db.refresh(new_reader)
    return new_reader


def get_reader_by_email(db: Session, reader_email: str):
    return db.query(Reader).filter(Reader.email == reader_email).first()


def get_reader_by_id(db: Session, reader_id: int):
    return db.query(Reader).filter(Reader.id == reader_id)


def update_reader(db: Session, reader_id: int, reader_data):
    reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if not reader:
        return None
    for key, value in reader_data.dict().items():
        setattr(reader, key, value)
    db.commit()
    db.refresh(reader)
    return reader


def delete_reader(db: Session, reader_id: int):
    reader = db.query(Reader).filter(Reader.id == reader_id).first()
    if not reader:
        return None
    db.delete(reader)
    db.commit()
    return reader
