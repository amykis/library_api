from pydantic import BaseModel
from typing import Optional


class ReaderBase(BaseModel):
    name: str
    email: str


class ReaderCreate(ReaderBase):
    pass


class ReaderResponse(ReaderBase):
    id: int

    model_config = {"from_attributes": True}
