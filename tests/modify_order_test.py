from fastapi.testclient import TestClient
from limit_order_api.main import app
from limit_order_api.db import engine
from limit_order_api.models import Base

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_modify_order_valid_input():
    response_place_order = client.post(
        "/place_order", json={"quantity": 10, "price": 100, "side": 1}
    )
    assert response_place_order.status_code == 200
    data = response_place_order.json()
    order_id = data["order_id"]

    response_modify_order = client.put(
        "/modify_order",
        json={"order_id": order_id, "updated_quantity": 15, "updated_price": 150},
    )
    assert response_modify_order.status_code == 200
    assert response_modify_order.json() == {"success": True}


def test_modify_order_invalid_quantity():
    response = client.put(
        "/modify_order",
        json={"order_id": 123, "updated_quantity": -5, "updated_price": 100},
    )
    assert response.json() == {"success": False}


def test_modify_order_invalid_price():
    response = client.put(
        "/modify_order",
        json={"order_id": 123, "updated_quantity": 10, "updated_price": -100},
    )
    assert response.json() == {"success": False}


def test_modify_order_order_not_found():
    response = client.put(
        "/modify_order",
        json={"order_id": 999, "updated_quantity": 10, "updated_price": 100},
    )
    assert response.json() == {"success": False}
