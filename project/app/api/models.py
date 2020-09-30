# project/app/api/models.py


from pydantic import BaseModel
from tortoise import fields, models


class TextSummary(models.Model):
    url = fields.TextField()
    textsummary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class SummaryPayloadSchema(BaseModel):
    url: str

class SummaryResponseSchema(SummaryPayloadSchema):
    id: int
