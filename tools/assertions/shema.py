from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

from tools.logger import get_logger

# Логгер для информации о процессе валидации
logger = get_logger("Проверка схемы")


@allure.step("Проверка правильности JSON схемы")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """"
    Проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме (schema)

    :param: instance (Any): JSON-объект, который необходимо проверить.
    :param: schema (dict): JSON-схема, согласно которой производится валидация.
    :raises:
        jsonschema.exceptions.ValidationError: В случае несоответствия JSON-объекта схеме.
        jsonschema.exceptions.SchemaError: Если переданная схема некорректна.
    """
    logger.info("Проверка правильности JSON схемы")

    # Выполняем валидацию JSON-объекта по заданной схеме
    validate(
        schema=schema,  # JSON-схема, задающая структуру данных
        instance=instance,  # Проверяемый JSON-объект
        format_checker=Draft202012Validator.FORMAT_CHECKER,  # Проверка форматов (например, email, дата и т.д.)
    )
