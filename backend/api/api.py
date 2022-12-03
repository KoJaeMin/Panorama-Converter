from fastapi import APIRouter
from api import front
# from fastapi.api import utils, singan

api_router = APIRouter()
api_router.include_router(front.router, prefix="", tags=["default"])
# api_router.include_router(train.router, prefix="/train", tags=["train"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])