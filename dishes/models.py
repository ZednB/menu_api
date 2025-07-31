import enum

from sqlalchemy import Column, Integer, String, Text, Float, Enum
from sqlalchemy.orm import relationship

from core.database import Base
from orders.models import order_dish_association


class DishCategory(str, enum.Enum):
    main = 'Основные блюда'
    dessert = 'Десерты'
    drink = 'Напитки'


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    category = Column(Enum(DishCategory), nullable=True)
    orders = relationship('Order', secondary=order_dish_association, back_populates='dishes')
