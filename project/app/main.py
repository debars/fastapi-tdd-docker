# project/app/main.py


from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.views import views
from app.config import config


app = FastAPI()

register_tortoise(
    app,
    db_url=config.database_url,
    modules={"models": ["app.api.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(views)
