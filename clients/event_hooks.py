from httpx import Request, Response

from tools.logger import get_logger

# Создаем логгер для HTTP-клиента
logger = get_logger("HTTP_CLIENT")


def log_request_event_hook(request: Request):
    """
    Логирует информацию перед отправкой HTTP-запроса
    """
    logger.info(f'Отправка запроса с методом {request.method} по адресу {request.url}')


def log_response_event_hook(response: Response):
    """
    Логирует информацию после получения HTTP-ответа.
    """
    logger.info(
        f"Получен ответ, код: {response.status_code}, состояние: {response.reason_phrase} от {response.url}\n"
    )
