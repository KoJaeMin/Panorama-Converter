from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse,JSONResponse
from core.train import train
from core.utils import save

router = APIRouter()

@router.post("/img",response_class=FileResponse)
async def create_file(img: UploadFile = File()):
    default_url = '/Users/gojaemin/Desktop/progject/Panorama-Converter/backend/'
    with open(img.filename, 'wb') as image:
        content = await img.read()
        image.write(content)
        image.close()
    return str(default_url+img.filename)