from typing import Optional, TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from orders.schemas import OrderRead


class DishBase(BaseModel):
    # id: int
    name: str
    description: Optional[str]
    price: float
    category: Optional[str] = None


class DishCreate(DishBase):
    order_id: Optional[int] = None

class DishRead(DishBase):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True
