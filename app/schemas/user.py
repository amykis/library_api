from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    model_config = {"from_attributes": True}


class UserUpdate(UserBase):
    email: Optional[str] = None
    password: Optional[str] = None
