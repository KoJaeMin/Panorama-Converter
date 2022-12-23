from pydantic import BaseModel
from core.train import trainer
from core.make import make

class BasicModel(BaseModel):
    username : str
    password : str
    filename : str

class CheckModel(BasicModel):
    count : int

class MakingModel(BasicModel):
    opt_h : int
    opt_w : int

class ResponseModel(BaseModel):
    status : int
    message : str
    
class Task:
    def __init__(self, height : int, width : int ,input_name : str, input_dir : str,trainmodel_dir: str, out : str, user_name : str = '0000'):
        self.train_status = False
        self.make_status = False
        
        self.height = height
        self.width = width
        self.input_name = input_name
        self.input_dir = input_dir
        self.trainmodel_dir = trainmodel_dir
        self.out = out
        self.user_name = user_name
        
    def StartTask(self):
        self.ChangeTrainStatus()
        trainer(input_name = self.input_name, input_dir = self.input_dir,trainmodel_dir = self.trainmodel_dir,out=self.out,user_name=self.user_name)
        self.ChangeTrainStatus()
        self.ChangeMakeStatus()
        make(height=self.height, width=self.width, input_name=self.input_name, input_dir=self.input_dir,trainmodel_dir=self.trainmodel_dir, out=self.out,user_name=self.user_name)
        self.ChangeMakeStatus()
    
    def GetTrainStatus(self) -> bool:
        return self.train_status
    
    def GetMakeStatus(self) -> bool:
        return self.make_status
    
    def ChangeTrainStatus(self) -> None:
        self.train_status = not self.train_status
        
    def ChangeMakeStatus(self) -> None:
        self.make_status = not self.make_status
        
    def IsFinished(self) -> bool:
        return not (self.GetTrainStatus() and self.GetMakeStatus())
    
# class TaskQueue:
#     def __init__(self):
#         self.queue = []
        
#     def AddTask(self):
#         if(not self.IsQueueEmpty()):
#             return "It's not Empty."
#         newTask = Task()
#         self.queue.append(newTask)
#         return "Add Complete."
            
#     def IsQueueEmpty(self) -> bool:
#         return len(self.queue) == 0
    
#     def DeleteTask(self):
#         if(self.queue[0].GetTrainStatus() or self.queue[0].GetMakeStatus()):
#             return "It's Runnig."
#         self.queue.pop()
#         return "Delete Complete."