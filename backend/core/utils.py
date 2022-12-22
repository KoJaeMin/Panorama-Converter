from fastapi import UploadFile

async def getimage(imagefile : str, img : UploadFile) -> None :
    with open(imagefile, 'wb') as image:
        content = await img.read()
        image.write(content)