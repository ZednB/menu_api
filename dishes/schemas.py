from typing import Optional

from pydantic import BaseModel


class DishBase(BaseModel):
    name: str
    description: Optional[str]
    price: float
    category: str


class DishCreate(DishBase):
    pass


class DishRead(DishBase):
    id: int

    class Config:
        orm_mode = True
