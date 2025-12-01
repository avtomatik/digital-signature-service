from fastapi import APIRouter

from app.services.redis import redis_client

router = APIRouter()


@router.get("/cache-test")
async def cache_test():
    await redis_client.set("my_key", "Hello, Redis!")
    value = await redis_client.get("my_key")
    return {"cached_value": value}
