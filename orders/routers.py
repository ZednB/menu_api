from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from orders import services
from orders.schemas import OrderRead, OrderCreate, OrderUpdate
from orders.services import get_orders, create_order, delete_order

router = APIRouter(prefix='/orders', tags=['orders'])


@router.post('/', response_model=OrderRead, status_code=201)
def create_order_view(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(order, db)


@router.get('/', response_model=List[OrderRead])
def orders_list(db: Session = Depends(get_db)):
    return get_orders(db)


@router.delete('/{order_id}')
def order_delete(order_id: int, db: Session = Depends(get_db)):
    success = delete_order(order_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"detail": "Order deleted successfully"}


@router.put('/{order_id}', response_model=OrderRead)
def update_order(order_id: int, order_data: OrderUpdate, db: Session = Depends(get_db)):
    return services.update_order(db, order_id, order_data)
