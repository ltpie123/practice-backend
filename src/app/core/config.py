from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="forbid",  # Ensures no unexpected fields are passed
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


# Load settings once
settings = get_settings()
print(settings.SQLALCHEMY_DATABASE_URL)  # Debugging output
