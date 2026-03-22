from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "OrderBot API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # GROQ
    GROQ_API_KEY: Optional[str] = None
    GROQ_MODEL: str = "llama-3.3-70b-versatile"
    
    # DB
    DATABASE_URL: str = "sqlite+aiosqlite:///./sql_app.db"
    
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

settings = Settings()
