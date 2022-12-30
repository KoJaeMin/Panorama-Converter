from typing import Union
from fastapi import APIRouter, File, Form, UploadFile, BackgroundTasks, Response, status
from fastapi.responses import FileResponse
from core.train import trainer
from core.utils import DownloadImage,IsQueueEmpty
from core.make import make
from core.check import *
from dotenv import load_dotenv
import os
from PIL import Image
from datatype.api import Task

load_dotenv()
router = APIRouter()

### global variable
input_dir = str(os.environ['INPUT_DIR'])
trainmodel_dir = str(os.environ['TRAIN_DIR'])
out = str(os.environ['OUTPUT_DIR'])
TaskQueue = []

@router.post("/training", status_code = 201)
async def training(height : int , width : int, username : str, password : str, response: Response, background_tasks: BackgroundTasks, img: UploadFile = File()):
    global input_dir
    global trainmodel_dir
    global out
    global TaskQueue
    if not CheckPassWord(password):
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"message": "Password is Incorrect."}
    if height < 0 or width < 0:
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"message": "Error : Please enter positive integer"}
    ### Input file 저장
    await DownloadImage(f"{input_dir}/{img.filename}", img)
    if(not IsQueueEmpty(TaskQueue)):
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"message": "Task Queue is full."}
    ### Generate Task
    newTask = Task(height=height, width= width, input_name=img.filename, input_dir=input_dir, trainmodel_dir=trainmodel_dir, out=out,user_name=username)
    TaskQueue.append(newTask)
    ### Start Task
    background_tasks.add_task(newTask.StartTask)
    return {"message": "Start Task."}


@router.get("/check", status_code = 202)
async def check(username : str, password : str, response: Response):
    global input_dir
    global trainmodel_dir
    global out
    global TaskQueue
    if CheckPassWord(password):
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"message": "Password is Incorrect."}
    if IsQueueEmpty(TaskQueue):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Task Queue is Empty."}
    if TaskQueue[0].IsFinished():
        TaskQueue.pop(0)
        response.status_code = status.HTTP_200_OK
        return {"message": "Task is done."}
    return {"message" : "Task is not done."}
    

# @router.get("/making", response_class=FileResponse)
@router.get("/download", status_code = 200)
async def download(filename: str, username : str, password : str,response: Response):
    global input_dir
    global trainmodel_dir
    global out
    if CheckPassWord(password):
        response.status_code = status.HTTP_403_FORBIDDEN
        return {"message": "Password is Incorrect."}
    file_halfname = filename[:-4]
    result_path = '%s/RandomSamples_ArbitrerySizes/%s/%s/%s.png' % (out,file_halfname, username, file_halfname)
    if not CheckExist(result_path):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "File is not Exist."}
    return FileResponse(file_halfname)