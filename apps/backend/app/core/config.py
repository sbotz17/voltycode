from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "VoltyCode API"
    app_version: str = "0.1.0"
    environment: str = "development"
    debug: bool = False

    api_v1_prefix: str = "/api/v1"

    database_url: str | None = Field(default=None, validation_alias="DATABASE_URL")
    supabase_url: str | None = Field(default=None, validation_alias="SUPABASE_URL")
    supabase_anon_key: str | None = Field(
        default=None,
        validation_alias="SUPABASE_ANON_KEY",
    )
    supabase_service_role_key: str | None = Field(
        default=None,
        validation_alias="SUPABASE_SERVICE_ROLE_KEY",
    )
    redis_url: str | None = Field(default=None, validation_alias="REDIS_URL")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
