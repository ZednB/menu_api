from fastapi import HTTPException
from sqlalchemy.orm import Session

from dishes.models import Dish
from orders.models import Order
from orders.schemas import OrderCreate, OrderUpdate


def get_order_by_id(order_id: int, db: Session):
    return db.query(Order).filter(Order.id == order_id).first()


def create_order(order_data: OrderCreate, db: Session) -> Order:
    dish_objects = db.query(Dish).filter(Dish.id.in_(order_data.dishes)).all()
    new_order = Order(
        customer_name=order_data.customer_name,
        order_time=order_data.order_time,
        status=order_data.status,
        dishes=dish_objects
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


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
    order = get_order_by_id(order_id, db)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order_update.customer_name is not None:
        order.customer_name = order_update.customer_name
    if order_update.order_time is not None:
        order.order_time = order_update.order_time
    if order_update.status is not None:
        order.status = order_update.status

    if order_update.dishes is not None:
        order.dishes.clear()
        for dish_id in order_update.dishes:
            dish = db.query(Dish).filter(Dish.id == dish_id).first()
            if not dish:
                raise HTTPException(status_code=404, detail=f"Dish with id {dish_id} not found")
            order.dishes.append(dish)
    db.commit()
    db.refresh(order)
    return order
