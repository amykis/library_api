from sqlalchemy import Column, Integer, String, CheckConstraint
from app.models.base import Base


class Book(Base):
    __tablename__ = "books"
    __table_args__ = (CheckConstraint('copies >= 0', name='check_copies_non_negative'),)

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    year = Column(Integer, nullable=True)
    isbn = Column(String(17), unique=True, nullable=True)
    copies = Column(Integer, nullable=False, default=1)
