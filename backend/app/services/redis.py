import redis.asyncio as redis

from app.core.config import settings

redis_client = redis.from_url(
    settings.cache_url, encoding="utf-8", decode_responses=True
)
