# project/app/main.py


from fastapi import APIRouter, Depends

from app.config import get_settings, Settings


views = APIRouter()


@views.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
