# project/app/main.py


from fastapi import FastAPI

from app.config import config

app = FastAPI()


@app.get("/ping")
async def pong():
    return {
        "ping": "pong!",
        "environment": config.environment,
        "testing": config.testing,
    }
