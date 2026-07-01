# Put all settings user .env variables here .
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")
    # App
    APP_NAME : str
    VERSION : str

    # Api's
    GROQ_API_KEY : str

    # File
    FILE_ALLOWED_TYPES : list[str]
    FILE_ALLOWED_SIZE : int
    FILE_CHUNK_SIZE : int

def get_settings () :
     return Settings()