from fastapi.testclient import TestClient
from limit_order_api.main import app

client = TestClient(app)


def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200
