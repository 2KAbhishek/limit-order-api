from fastapi.testclient import TestClient
from limit_order_api.main import app
from limit_order_api.db import engine, SessionLocal
from limit_order_api.models import Base, Trade

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_cancel_order_valid_input():
    response_place_order = client.post(
        "/place_order", json={"quantity": 10, "price": 100, "side": 1}
    )
    data = response_place_order.json()
    order_id = data["order_id"]

    response_cancel_order = client.delete(f"/cancel_order/{order_id}")
    assert response_cancel_order.status_code == 200
    assert response_cancel_order.json() == {"success": True}


def test_cancel_order_order_not_found():
    response = client.delete("/cancel_order/999")
    assert response.json() == {"success": False}


def test_cancel_order_order_already_traded():
    response_place_order = client.post(
        "/place_order", json={"quantity": 10, "price": 100, "side": 1}
    )
    assert response_place_order.status_code == 200
    data = response_place_order.json()
    order_id = data["order_id"]

    with SessionLocal() as session:
        trade = Trade(
            execution_timestamp=123,
            price=100,
            qty=10,
            bid_order_id=order_id,
            ask_order_id=1,
        )
        session.add(trade)
        session.commit()

    response_cancel_order = client.delete(f"/cancel_order/{order_id}")
    assert response_cancel_order.json() == {"success": False}
