from fastapi import APIRouter
from api import front, panorama

api_router = APIRouter()
api_router.include_router(front.router, prefix="", tags=["default"])
api_router.include_router(panorama.router, prefix="/panorama", tags=["panorama"])