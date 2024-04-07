from sqlalchemy import Column, Integer, Float
from pydantic import BaseModel
from limit_order_api.db import Base


class PlaceOrderRequest(BaseModel):
    quantity: int
    price: float
    side: int


class ModifyOrderRequest(BaseModel):
    order_id: int
    updated_quantity: int
    updated_price: float


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    side = Column(Integer)
