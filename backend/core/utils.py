def getimage(imagefile : str) -> None :
    with open(imagefile, 'wb') as image:
        content = imagefile.read()
        image.write(content)