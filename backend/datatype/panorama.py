from pydantic import BaseModel

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