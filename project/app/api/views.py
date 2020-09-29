# project/app/main.py


from fastapi import APIRouter

from app.config import config


views = APIRouter()


@views.get("/ping")
async def pong():
    return {
        "ping": "pong!",
        "environment": config.environment,
        "testing": config.testing,
    }
