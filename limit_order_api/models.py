from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from sqlalchemy.orm import declarative_base

Base = declarative_base()


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


class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True, index=True)
    execution_timestamp = Column(Integer)
    price = Column(Float)
    qty = Column(Integer)
    bid_order_id = Column(Integer, ForeignKey("orders.id"))
    ask_order_id = Column(Integer, ForeignKey("orders.id"))
    bid_order = relationship("Order", foreign_keys=[bid_order_id])
    ask_order = relationship("Order", foreign_keys=[ask_order_id])
