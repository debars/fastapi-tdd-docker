# project/app/api/views.py


from typing import List
from fastapi import APIRouter, Depends
from fastapi import HTTPException

from app.config import get_settings, Settings
from app.api.models import SummaryPayloadSchema, SummaryResponseSchema
from app.api.models import SummarySchema
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

@views.post("/summaries/", tags=["summaries"], response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    print("create_summary")
    summary_id = await crud.post(payload)

    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    return response_object

@views.get("/summaries/{id}/", response_model=SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary

@views.get("/summaries/", response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    return await crud.get_all()

