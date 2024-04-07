from fastapi.testclient import TestClient
from limit_order_api.main import app
from limit_order_api.db import engine
from limit_order_api.models import Base

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_place_order_valid_input():
    response = client.post(
        "/place_order", json={"quantity": 10, "price": 100, "side": 1}
    )
    assert response.status_code == 200
    data = response.json()
    assert "order_id" in data


def test_place_order_invalid_quantity():
    response = client.post(
        "/place_order", json={"quantity": -5, "price": 100, "side": 1}
    )
    assert response.status_code == 400


def test_place_order_invalid_price():
    response = client.post(
        "/place_order", json={"quantity": 10, "price": -100, "side": 1}
    )
    assert response.status_code == 400


def test_place_order_invalid_side():
    response = client.post(
        "/place_order", json={"quantity": 10, "price": 100, "side": 0}
    )
    assert response.status_code == 400


def test_place_order_edge_case():
    # Test with quantity = 0
    response = client.post(
        "/place_order", json={"quantity": 0, "price": 100, "side": 1}
    )
    assert response.status_code == 400

    # Test with price = 0
    response = client.post("/place_order", json={"quantity": 10, "price": 0, "side": 1})
    assert response.status_code == 400

    # Test with invalid side (neither 1 nor -1)
    response = client.post(
        "/place_order", json={"quantity": 10, "price": 100, "side": 2}
    )
    assert response.status_code == 400
