from typing import Union
from fastapi import APIRouter, File, Form, UploadFile, BackgroundTasks
from fastapi.responses import FileResponse
from core.train import trainer
from core.utils import DownloadImage,IsQueueEmpty
from core.make import make
from dotenv import load_dotenv
import os
from PIL import Image
from datatype.panorama import CheckModel, MakingModel, Task

load_dotenv()
router = APIRouter()

### global variable
input_dir = str(os.environ['INPUT_DIR'])
trainmodel_dir = str(os.environ['TRAIN_DIR'])
out = str(os.environ['OUTPUT_DIR'])
pw = os.environ['PW']
TaskQueue = []

@router.post("/training")
async def training(height : int , width : int, username : str, password : str, background_tasks: BackgroundTasks, img: UploadFile = File()):
    global pw
    global input_dir
    global trainmodel_dir
    global out
    global TaskQueue
    if password != pw:
        return {403, "Password is Incorrect."}
    user_name = f"{img.filename[:-4]}{username}"
    ### Input file 저장
    await DownloadImage(f"{input_dir}/{img.filename}", img)
    if(not IsQueueEmpty(TaskQueue)):
        return {403, "Task Queue is full."}
    ### Generate Task
    newTask = Task(height=height, width= width, input_name=img.filename, input_dir=input_dir, trainmodel_dir=trainmodel_dir, out=out,user_name=user_name)
    TaskQueue.append(newTask)
    ### Start Task
    background_tasks.add_task(newTask.StartTask)
    return {202, "Start Task."}


@router.post("/check")
async def check(checkmodel : CheckModel):
    global pw
    global input_dir
    global trainmodel_dir
    global out
    global TaskQueue
    if checkmodel.password != pw:
        return {403, "Password is Incorrect."}
    if IsQueueEmpty(TaskQueue):
        return {404, "Task Queue is Empty."}
    if TaskQueue[0].IsFinished():
        TaskQueue.pop(0)
        return {200, "Task is done."}
    return {202, "Task is not done."}
    

# @router.get("/making", response_class=FileResponse)
@router.post("/making")
async def making(makingmodel : MakingModel):
    global pw
    global input_dir
    global trainmodel_dir
    global out
    if makingmodel.password != pw:
        return {403, "Password is Incorrect."}