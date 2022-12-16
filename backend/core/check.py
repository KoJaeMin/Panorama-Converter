import os

def CheckFile(filepath : str) -> bool:
    if not CheckExist(filepath):
        return False
    return os.path.isfile(filepath)

def CheckExist(dir : str) -> bool:
    return os.path.exists(dir)