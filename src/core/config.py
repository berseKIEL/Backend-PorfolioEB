from pydantic import BaseSettings, AnyHttpUrl
from typing import List

import os
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    API_V1_ROUTE: str = "/api/v1"
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY')
    JWT_REFRESH_SECRET_KEY: str = os.getenv('JWT_REFRESH_SECRET_KEY')
    ALGORITH = "HS256"
    ACCESS_TOKEN_EXPIRATION: int = 15
    REFRESH_TOKEN_EXPIRES_MINUTES: int = 60 * 24 * 7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Porfolio FARM Exequiel Barco"

    MONGO_CONNECTION: str = os.getenv('MONGO_CONNECTION')

    class Config:
        case_sensitive = True


settings = Settings()
