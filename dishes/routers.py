from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dishes.schemas import DishRead, DishCreate
from dishes.services import get_dishes, delete_dishes, create_dish
from core.database import get_db

router = APIRouter(prefix='/dishes', tags=['dishes'])


@router.post('/', response_model=DishRead)
def create_dish_view(dish: DishCreate, db: Session = Depends(get_db)):
    return create_dish(dish, db)


@router.get("/", response_model=List[DishRead])
def dishes_list(db: Session = Depends(get_db)):
    return get_dishes(db)


@router.delete("/{dish_id}")
def remove_dish(dish_id: int, db: Session = Depends(get_db)):
    success = delete_dishes(dish_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="Dish not found")
    return {"detail": "Dish deleted successfully"}
