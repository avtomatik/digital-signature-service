from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "mysecretpassword"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "digital_signature_service"

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "mysecretpassword"
    POSTGRES_DB: str = "digital_signature_service"

    MQ_USER: str = "guest"
    MQ_PASSWORD: str = "guest"
    MQ_HOST: str = "rabbitmq"
    MQ_PORT: str = "5672"

    REDIS_HOST: str = "localhost"
    REDIS_PORT: str = "6379"
    REDIS_DB: str = "0"

    @property
    def db_dsn(self) -> str:
        return (
            f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    @property
    def mq_url(self) -> str:
        return (
            f"amqp://{self.MQ_USER}:{self.MQ_PASSWORD}@"
            f"{self.MQ_HOST}:{self.MQ_PORT}/"
        )

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    class Config(ConfigDict):
        env_file = ".env"


settings = Settings()
