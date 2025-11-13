import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL = os.getenv(
        "DATABASE_URL", "postgresql://user:password@postgres:5432/ds_service"
    )
    RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/")
    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")


settings = Settings()
