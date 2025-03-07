from fastapi import FastAPI

from app.api.item import item_router
from app.api.thing import thing_router
from app.core.config import settings


app = FastAPI(title=settings.app_title)

app.include_router(item_router)
app.include_router(thing_router)
