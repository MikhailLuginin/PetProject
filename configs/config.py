import json
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    base_url: str = "https://practice.expandtesting.com/notes"

    @property
    def api_url(self) -> str:
        return f'{self.base_url}'


base_settings = Settings()

# Файл строго в configs/
DATA_FILE = Path(__file__).resolve().parent / "data_user.json"


class DataUser:

    @classmethod
    def load(cls) -> dict:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def save(cls, data: dict):
        with DATA_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def user_id(cls):
        return cls.load().get("user_id")

    @classmethod
    def user_name(cls):
        return cls.load().get("name")

    @classmethod
    def user_email(cls):
        return cls.load().get("email")

    @classmethod
    def user_password(cls):
        return cls.load().get("password")

    @classmethod
    def user_token(cls):
        return cls.load().get("token")

    @classmethod
    def set_token(cls, token: str):
        """Обновляем токен в файле data_user.json"""
        data = cls.load()
        data["token"] = token
        cls.save(data)
