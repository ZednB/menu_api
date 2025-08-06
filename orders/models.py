import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, Enum
from sqlalchemy.orm import relationship

from core.database import Base


class StatusOrder(str, enum.Enum):
    processing = 'В обработке'
    getting_ready = 'Готовится'
    delivering = 'Доставляется'
    done = 'Завершен'


order_dish_association = Table(
    'order_dish_association',
    Base.metadata,
    Column('order_id', ForeignKey('orders.id'), primary_key=True),
    Column('dish_id', ForeignKey('dishes.id'), primary_key=True)
)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(50), nullable=True)
    dishes = relationship('Dish', secondary=order_dish_association, back_populates='orders')
    order_time = Column(DateTime, nullable=False)
    status = Column(Enum(StatusOrder))


