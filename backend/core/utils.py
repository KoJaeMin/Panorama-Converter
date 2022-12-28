from fastapi import UploadFile
from PIL import Image

async def DownloadImage(imagefile : str, img : UploadFile) -> None :
    with open(imagefile, 'wb') as image:
        content = await img.read()
        image.write(content)
        
def IsQueueEmpty(queue : list) -> bool:
    return len(queue) == 0

def ResizeImg(img_path: str, height : int, width : int) -> None:
    img = Image.open(img_path)
    img_resize_lanczos = img.resize((width, height), Image.LANCZOS)
    img_resize_lanczos.save(img_path)