from fastapi import UploadFile

async def DownloadImage(imagefile : str, img : UploadFile) -> None :
    with open(imagefile, 'wb') as image:
        content = await img.read()
        image.write(content)
        
def IsQueueEmpty(queue : list) -> bool:
    return len(queue) == 0