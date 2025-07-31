import os

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: str = '5432'
    DB_NAME: str = 'menu_api'
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = '1111'

    @property
    def database_url(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = '.env'


settings = Settings()
