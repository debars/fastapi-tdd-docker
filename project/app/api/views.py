# project/app/main.py


from fastapi import APIRouter, Depends

from app.config import get_settings, Settings
from app.api.models import SummaryPayloadSchema, SummaryResponseSchema
from app.api import crud


views = APIRouter()


@views.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    print("pong")
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }

@views.post("/summaries", tags=["summaries"], response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    print("create_summary")
    summary_id = await crud.post(payload)

    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    return response_object
