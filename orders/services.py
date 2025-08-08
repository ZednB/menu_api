from fastapi import HTTPException
from sqlalchemy.orm import Session

from dishes.models import Dish
from orders.constants import STATUS_FLOW
from orders.models import Order
from orders.schemas import OrderCreate, OrderUpdate


def get_order_by_id(order_id: int, db: Session):
    return db.query(Order).filter(Order.id == order_id).first()


def create_order(order_data: OrderCreate, db: Session) -> Order:
    order = Order(
        customer_name=order_data.customer_name,
        order_time=order_data.order_time,
        status='В обработке',
    )
    for dish_id in order_data.dishes:
        dish = db.query(Dish).filter(Dish.id == dish_id).first()
        if not dish:
            raise HTTPException(status_code=400, detail=f"Блюдо с id {dish_id} не найдено")
        order.dishes.append(dish)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_orders(db: Session):
    return db.query(Order).all()


def delete_order(order_id: int, db: Session):
    order = get_order_by_id(order_id, db)
    if order:
        db.delete(order)
        db.commit()
        return True
    return False


def update_order(db: Session, order_id: int, order_update: OrderUpdate):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail=f"Заказ с таким id {order_id} не найден")
    if order_update.customer_name is not None:
        order.customer_name = order_update.customer_name
    if order_update.order_time is not None:
        order.order_time = order_update.order_time
    if order_update.status:
        if order_update.status not in STATUS_FLOW:
            raise HTTPException(status_code=400, detail="Неправильный статус")
        if order_update.status == 'Отменен' and order_update.status != 'В обработке':
            raise HTTPException(status_code=400, detail="Заказ можно отменить только в статусе 'В обработке'")
        allowed_next = STATUS_FLOW.get(order.status, [])
        if order_update.status not in allowed_next:
            raise HTTPException(status_code=400,
                                detail=f"Неправильное изменение статуса: "
                                       f"'{order.status}' -> '{order_update.status}'")
        order.status = order_update.status
    if order_update.dishes is not None:
        order.dishes.clear()
        for dish_id in order_update.dishes:
            dish = db.query(Dish).filter(Dish.id == dish_id).first()
            if not dish:
                raise HTTPException(status_code=404, detail=f"Блюдо с id {dish_id} не найдено")
            order.dishes.append(dish)
    db.commit()
    db.refresh(order)
    return order
