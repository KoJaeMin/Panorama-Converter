import os
from dotenv import load_dotenv

load_dotenv()

def CheckFile(filepath : str) -> bool:
    if not CheckExist(filepath):
        return False
    return os.path.isfile(filepath)

def CheckExist(dir : str) -> bool:
    return os.path.exists(dir)

def CheckPassWord(password : str) -> bool:
    pw = os.environ['PW']
    return password == pw