from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parent
router = APIRouter()
templates = Jinja2Templates(directory=str(BASE_PATH.resolve().parent / "templates"))
router.mount(str(BASE_PATH.resolve().parent /"static"), StaticFiles(directory=str(BASE_PATH.resolve().parent /"static")), name="static")


@router.get("/", response_class=HTMLResponse)
def read_root(request : Request):
    print(str(BASE_PATH.resolve().parent /"static"))
    return templates.TemplateResponse("index.html",{"request": request}) 