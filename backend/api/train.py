from fastapi import APIRouter, File, Form, UploadFile

router = APIRouter()

@router.get("/")
async def create_file(file: bytes = File(), fileb: UploadFile = File(), token: str = Form()):
    contents = await myfile.read()
    return {"file_size": len(file),"token": token,"fileb_content_type": fileb.content_type,}