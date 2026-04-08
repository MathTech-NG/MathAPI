from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./mathapi.db"
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "change-me"
    api_rate_limit: int = 100
    environment: str = "development"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
