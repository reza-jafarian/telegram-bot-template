from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_ignore_empty=True)

    BOT_TOKEN         : str
    API_HASH          : str
    API_ID            : int
    
    SESSION_NAME      : str = 'bot'
    DB_PATH           : str = 'database.db'
    OWNER             : int
    
    DATABASE_NAME     : str
    DATABASE_USERNAME : str
    DATABASE_PASSWORD : str


BASE_DIR = Path(__file__).resolve().parent.parent.parent
settings = Settings()