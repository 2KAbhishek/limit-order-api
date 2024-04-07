from fastapi import FastAPI
from uvicorn import run
from fastapi.openapi.utils import get_openapi


app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="limit-order-api",
        version="0.1.0",
        description="API to demonstrate limit order book functionality",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


def start():
    run("limit_order_api.main:app", host="0.0.0.0", port=8000, reload=True)
