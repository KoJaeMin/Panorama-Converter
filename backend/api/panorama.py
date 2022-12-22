from typing import Union
from fastapi import APIRouter, File, Form, UploadFile, BackgroundTasks
from fastapi.responses import FileResponse
from core.train import trainer
from core.utils import getimage
from core.make import make
from dotenv import load_dotenv
import os
from PIL import Image
from datatype.panorama import CheckModel, MakingModel, CustomResponseModel

load_dotenv()
router = APIRouter()

### global variable
input_dir = str(os.environ['INPUT_DIR'])
trainmodel_dir = str(os.environ['TRAIN_DIR'])
out = str(os.environ['OUTPUT_DIR'])
pw = os.environ['PW']

@router.post("/training")
async def training(username : str, password : str, background_tasks: BackgroundTasks, img: UploadFile = File()):
    global pw
    global input_dir
    global trainmodel_dir
    global out
    if password != pw:
        return {403, "Password is Incorrect."}
    user_name = f"{img.filename[:-4]}{username}"
    ### Input file 저장
    await getimage(f"{input_dir}/{img.filename}", img)
    ### train
    background_tasks.add_task(trainer, input_name = img.filename ,input_dir = input_dir,trainmodel_dir = trainmodel_dir, out=out,  user_name = user_name)
    return {202, "Start training..."}


@router.post("/check")
async def check(checkmodel : CheckModel):
    global pw
    global input_dir
    global trainmodel_dir
    global out
    if checkmodel.password != pw:
        return {403, "Password is Incorrect."}
    # return {"message" : }
        # user_name = f"{img.filename[:-4]}{username}"
        # ### make
        # make(height = opt_h, width = opt_w ,input_name =img,input_dir = input_dir,trainmodel_dir = trainmodel_dir,out=out,  user_name = user_name)
        # ### resize
        # output_folder = f'{out}/RandomSamples_ArbitrerySizes/{img.filename[:-4]}/{user_name}'
        # default_name = '0.png'
        # image = Image.open(f"{output_folder}/{default_name}")
        # img_resize_lanczos = image.resize((opt_w, opt_h), Image.LANCZOS)
        # img_resize_lanczos.save(f'{output_folder}/{img.filename[:-4]}.png')
        # return f'{output_folder}/{img.filename[:-4]}.png'

# @router.get("/making", response_class=FileResponse)
@router.post("/making")
async def making(makingmodel : MakingModel):
    global pw
    global input_dir
    global trainmodel_dir
    global out
    if makingmodel.password != pw:
        return {403, "Password is Incorrect."}
        # user_name = f"{img.filename[:-4]}{username}"
        # ### make
        # make(height = opt_h, width = opt_w ,input_name =img,input_dir = input_dir,trainmodel_dir = trainmodel_dir,out=out,  user_name = user_name)
        # ### resize
        # output_folder = f'{out}/RandomSamples_ArbitrerySizes/{img.filename[:-4]}/{user_name}'
        # default_name = '0.png'
        # image = Image.open(f"{output_folder}/{default_name}")
        # img_resize_lanczos = image.resize((opt_w, opt_h), Image.LANCZOS)
        # img_resize_lanczos.save(f'{output_folder}/{img.filename[:-4]}.png')
        # return f'{output_folder}/{img.filename[:-4]}.png'