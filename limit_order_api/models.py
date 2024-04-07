from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float
from pydantic import BaseModel

Base = declarative_base()


class OrderRequest(BaseModel):
    quantity: int
    price: float
    side: int


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    side = Column(Integer)
