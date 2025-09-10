import pytest

from configs.config import Settings


@pytest.fixture(scope="session")
def settings() -> Settings:
    """
    Фикстура создаёт объект с настройками один раз на всю тестовую сессию
    Экземпляр класса Settings с загруженными конфигурациями, по факту только base_url
    """
    return Settings()
