import alembic.config
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from uvicorn import run

from limit_order_api.db import database
from limit_order_api.routes import router as order_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await database.connect()
        yield
    finally:
        await database.disconnect()


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


def start():
    run("limit_order_api.main:app", host="0.0.0.0", port=8000, reload=True)


app = FastAPI(title="limit-order-api", lifespan=lifespan)
alembic.config.main(argv=["upgrade", "head"])
app.include_router(order_router)
app.openapi = custom_openapi
