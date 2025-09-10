from httpx import Client

from clients.event_hooks import log_request_event_hook, log_response_event_hook
from configs.config import base_settings


def get_http_client() -> Client:
    """
    Функция для инициализации HTTP-клиента
    """

    return Client(
        base_url=base_settings.base_url,  # Базовый URL для API
        event_hooks={
            "request": [log_request_event_hook],  # Логирование перед запросом
            "response": [log_response_event_hook]  # Логирование после ответа
        }
    )
