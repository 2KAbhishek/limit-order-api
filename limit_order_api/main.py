from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

def start():
    run("limit_order_api.main:app", host="0.0.0.0", port=8000, reload=True)
