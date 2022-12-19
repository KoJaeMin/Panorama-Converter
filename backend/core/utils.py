def getimage(imagefile : str) -> None :
    with open(imagefile, 'wb') as image:
        content = image.read()
        image.write(content)
        
# def getimage(imagefile : str, img : str) -> None:
#     with open(imagefile, 'rb') as image:
#         with open(img, 'wb') as result:
#             content = image.read()
#             result.write(content)