from fastapi import APIRouter

from app.api.routes_cache import router as cache_router
from app.api.routes_rabbitmq import router as rabbit_router
from app.api.routes_sign import router as sign_router

api_router = APIRouter()

api_router.include_router(cache_router, prefix="/cache", tags=["cache"])
api_router.include_router(rabbit_router, prefix="/mq", tags=["rabbitmq"])
api_router.include_router(sign_router, prefix="/sign", tags=["sign"])
