from fastapi.testclient import TestClient
from limit_order_api.main import app
from limit_order_api.db import engine, SessionLocal
from limit_order_api.models import Base, Order

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_fetch_all_orders():
    order_count = SessionLocal().query(Order).count()

    client.post("/place_order", json={"quantity": 10, "price": 100, "side": 1})
    res = client.get("/fetch_all_orders").json()
    assert len(res) == order_count + 1
