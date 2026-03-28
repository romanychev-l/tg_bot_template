from pymongo import AsyncMongoClient
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    TOKEN: SecretStr
    MONGO_HOST: str = "localhost"
    MONGO_PORT: int = 27017
    MONGO_DB_NAME: str = "bot_db"
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


config_settings = Settings()

mongo_client = AsyncMongoClient(config_settings.MONGO_HOST, config_settings.MONGO_PORT)
db = mongo_client[config_settings.MONGO_DB_NAME]
