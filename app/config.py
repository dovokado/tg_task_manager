from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    telegram_bot_token: str = ""
    gemini_api_key: str = ""
    vikunja_api_url: str = ""
    vikunja_api_token: str = ""
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/tg_task_manager"


settings = Settings()
