from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SPOTIPY_CLIENT_ID: str
    SPOTIPY_CLIENT_SECRET: str
    SPOTIPY_REDIRECT_URI: str
    SPOTIPY_SCOPE: str
    SPOTIPY_GENRES: List[str]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
