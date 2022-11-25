from fastapi import APIRouter

from fastapi.api import utils, singan

api_router = APIRouter()
api_router.include_router(train.router, prefix="/train", tags=["train"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])