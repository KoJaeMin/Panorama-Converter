from typing import Union

from fastapi import FastAPI
from api.api import api_router

from fastapi.staticfiles import StaticFiles
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent

app = FastAPI()

app.mount("/static", StaticFiles(directory=str(BASE_PATH/"frontend/static")), name="static")

app.include_router(api_router, prefix='')