from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parent

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def read_root(request : Request):
    return templates.TemplateResponse("index.html",{"request": request}) 