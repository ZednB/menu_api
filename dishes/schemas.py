from typing import Optional, TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from orders.schemas import OrderRead


class DishBase(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    category: str


class DishCreate(DishBase):
    order_id: Optional[int] = None


class DishRead(DishBase):
    id: int

    class Config:
        from_attributes = True


DishRead.model_rebuild()
