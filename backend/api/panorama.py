from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse
from core.train import trainer
from core.make import make
from dotenv import load_dotenv
import os
from PIL import Image
# from core.utils import save

load_dotenv()
router = APIRouter()

@router.post("/img",response_class=FileResponse)
async def training(username : str, password : str, opt_h : int , opt_w :int, img: UploadFile = File()):
    if password == os.environ['PW']:
        user_name = f"{img.filename[:-4]}{username}"
        input_dir = str(os.environ['INPUT_DIR'])
        out=str(os.environ['OUTPUT_DIR'])
        trainmodel_dir = str(os.environ['TRAINEDMOEDL_DIR'])
        ### Input file 저장
        with open(f"{input_dir}/{img.filename}", 'wb') as image:
            content = await img.read()
            image.write(content)
            image.close()
        ### train
        trainer(input_name = img.filename,input_dir = input_dir,out=out, trainmodel_dir = trainmodel_dir, user_name = user_name)
        ### make
        make(height = opt_h, width = opt_w ,input_name =img.filename,input_dir = input_dir,out=out, trainmodel_dir = trainmodel_dir, user_name = user_name)
        ### resize
        output_folder = f'{out}/RandomSamples_ArbitrerySizes/{img.filename[:-4]}/{user_name}'
        default_name = '0.png'
        img = Image.open(f"{output_folder}/{default_name}")
        img_resize_lanczos = img.resize((opt_w, opt_h), Image.LANCZOS)
        img_resize_lanczos.save(f'{output_folder}/{img.filename[:-4]}.png')
        return f'{output_folder}/{img.filename[:-4]}.png'
