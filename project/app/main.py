# project/app/main.py

import logging

from fastapi import FastAPI

from app.api.views import views
from app.db import init_db

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(views)
    return application


app = create_application()


@app.on_event("startup")
async def startup():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown():
    log.info("Shutting down...")
