from fastapi import APIRouter, HTTPException
from limit_order_api.db import SessionLocal
from limit_order_api.models import Order, PlaceOrderRequest, ModifyOrderRequest

router = APIRouter()


@router.post("/place_order")
async def place_order(order: PlaceOrderRequest):
    quantity = order.quantity
    price = order.price
    side = order.side

    if quantity <= 0 or price <= 0 or side not in [-1, 1]:
        raise HTTPException(status_code=400, detail="Invalid input")

    new_order = Order(quantity=quantity, price=price, side=side)

    with SessionLocal() as session:
        session.add(new_order)
        session.commit()

    return {"order_id": new_order.id}


@router.put("/modify_order")
async def modify_order(order: ModifyOrderRequest):
    order_id = order.order_id
    updated_quantity = order.updated_quantity
    updated_price = order.updated_price

    with SessionLocal() as session:
        order = session.get(Order, order_id)
        if order is None or updated_quantity <= 0 or updated_price <= 0:
            return {"success": False}

        updated_order = order
        updated_order.quantity = updated_quantity
        updated_order.price = updated_price
        session.commit()

    return {"success": True}
