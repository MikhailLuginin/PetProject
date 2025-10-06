import os
from pydantic_settings import BaseSettings
from dotenv import set_key


class Settings(BaseSettings):

    base_url: str = "https://practice.expandtesting.com"

    @property
    def api_url(self) -> str:
        return f'{self.base_url}'


base_settings = Settings()

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
ENV_PATH = os.path.join(PROJECT_ROOT, ".env")


def update_env(data: dict):
    """Обновляет переменные в .env файле"""
    for key, value in data.items():
        if value is None:
            value = ""
        set_key(ENV_PATH, key, str(value))
