# project/app/main.py


from fastapi import FastAPI

from app.api.views import views


app = FastAPI()

app.include_router(views)
