from fastapi import APIRouter, HTTPException
from limit_order_api.db import database
from limit_order_api.models import Order, OrderRequest

router = APIRouter()


@router.post("/place_order")
async def place_order(order: OrderRequest):
    quantity = order.quantity
    price = order.price
    side = order.side
    if quantity <= 0 or price <= 0 or side not in [-1, 1]:
        raise HTTPException(status_code=400, detail="Invalid input")

    query = Order.__table__.insert().values(quantity=quantity, price=price, side=side)
    order_id = await database.execute(query)
    return {"order_id": order_id}
