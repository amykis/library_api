from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.crud import user as crud_user
from app.core.database import get_db

router = APIRouter()


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud_user.get_all_users(db)


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, user)


@router.get('/by-email', response_model=UserResponse)
def get_user_by_email(user_email: str, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_email(db, user_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get('/{user_id}', response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    return crud_user.update_user(db, user_id, user_data)


@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud_user.delete_user(db, user_id)
