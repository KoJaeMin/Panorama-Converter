from typing import Union

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config import settings
from api.api import api_router

from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent

app = FastAPI()

app.mount("/static", StaticFiles(directory=str(BASE_PATH/"frontend/static")), name="static")

app.include_router(api_router, prefix='')

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# @app.post("/file")
# async def create_file(file: bytes = File(), fileb: UploadFile = File(), token: str = Form()):
#     return {"file_size": len(file),"token": token,"fileb_content_type": fileb.content_type,}

# @app.get("/file/{file_name}",response_class=FileResponse)
# async def main(file_name : str):
#     return "/home/jaemin/Panorama-Converter/Output/RandomSamples_ArbitrerySizes/people/epoch_500_max_200_Adam/scale_v=1.000000_scale_h=1.500000/0.png"
