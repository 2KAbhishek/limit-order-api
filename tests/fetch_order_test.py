from fastapi.testclient import TestClient
from limit_order_api.db import engine
from limit_order_api.models import Base
from limit_order_api.main import app

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_fetch_order_valid_input():
    response_place_order = client.post(
        "/place_order", json={"quantity": 10, "price": 100, "side": 1}
    )
    assert response_place_order.status_code == 200
    data = response_place_order.json()
    order_id = data["order_id"]

    response_fetch_order = client.get(f"/fetch_order/{order_id}")
    assert response_fetch_order.status_code == 200
    data = response_fetch_order.json()
    assert "order_id" in data
    assert "order_quantity" in data
    assert "average_traded_price" in data
    assert "order_alive" in data


def test_fetch_order_order_not_found():
    response = client.get("/fetch_order/999")
    assert response.status_code == 404
