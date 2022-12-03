from pydantic import BaseSettings
from dotenv import load_dotenv
import os
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

load_dotenv()

class Settings(BaseSettings):
    #### 60 minutes * 24 hours = 1 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    POSTGRES_HOST: str = os.environ['DB_HOST']
    POSTGRES_PORT: str = os.environ['DB_PORT']
    POSTGRES_USER: str = os.environ['DB_USER']
    POSTGRES_PASSWORD: str = os.environ['DB_PW']
    POSTGRES_DB: str = os.environ['DB_DB']
    # SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

settings = Settings()