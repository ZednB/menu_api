from typing import List, TYPE_CHECKING, Optional
from pydantic import BaseModel
from datetime import datetime

if TYPE_CHECKING:
    from dishes.schemas import DishRead


class OrderBase(BaseModel):
    id: int
    customer_name: str
    order_time: datetime
    status: str


class OrderCreate(OrderBase):
    dishes: List[int]


class OrderRead(OrderBase):
    id: int

    class Config:
        from_attributes = True


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    order_time: Optional[datetime] = None
    status: Optional[str] = None
    dishes: Optional[List[int]] = None


OrderRead.model_rebuild()
