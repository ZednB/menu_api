from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from dishes.models import Dish
from dishes.schemas import DishCreate


def create_dish(dish_data: DishCreate, db: Session) -> Dish:
    new_dish = Dish(
        name=dish_data.name,
        description=dish_data.description,
        price=dish_data.price,
        order_id=dish_data.order_id
    )
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return new_dish


def get_dishes(db: Session):
    return db.query(Dish).all()


def get_dish_by_id(dish_id: int, db: Session):
    return db.query(Dish).filter(Dish.id == dish_id).first()


def delete_dishes(dish_id: int, db: Session) -> bool:
    dish = get_dish_by_id(dish_id, db)
    if dish:
        db.delete(dish)
        db.commit()
        return True
    return False
