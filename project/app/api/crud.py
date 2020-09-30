# project/app/api/crud.py


from app.api.models import TextSummary
from app.api.models import SummaryPayloadSchema


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        textsummary="dummy summary",
    )
    await summary.save()
    return summary.id
