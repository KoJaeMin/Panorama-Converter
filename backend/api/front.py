from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent.parent

router = APIRouter()
templates = Jinja2Templates(directory=str(BASE_PATH/"frontend/templates"))

@router.get("/", response_class=HTMLResponse)
def read_root(request : Request):
    uri = '/panorama/img'
    return templates.TemplateResponse("index.html",{"request": request, "uri" : uri}) 