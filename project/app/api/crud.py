# project/app/api/crud.py


from typing import Union, List

from app.api.models import TextSummary
from app.api.models import SummaryPayloadSchema


async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    return None


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        textsummary="dummy summary",
    )
    await summary.save()
    return summary.id


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries
