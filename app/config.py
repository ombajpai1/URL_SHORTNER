from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME:str="Distributed URL Shortner"
    BASE_URL:str="http://localhost:8000"
    DATABASE_URL:str="sqlite+aiosqlite:///.url_shortner.db"

    model_config=SettingsConfigDict(env_file=".env", extra="ignore")

Settings=Settings()

