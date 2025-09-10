import allure

from configs.config import DataUser
from schemas.user.user_schemas import *
from tools.assertions.base import assert_equal
from tools.logger import get_logger

logger = get_logger("Проверка юзера")


@allure.step("Проверка создания пользователя")
def assert_create_user(
        actual: UserSchema,
        expected: CreateUserSchema
):
    """
    Проверяет, что данные, возвращённые API после создания юзера, соответствуют ожидаемым.

    :param: actual (UserSchema): Фактические данные юзера.
    :param: expected (CreateUserSchema и данные из сваггера): Ожидаемые данные.
    :raises: AssertionError: Если значения полей не совпадают.
    """
    logger.info("Проверка создания пользователя")

    assert_equal(actual.data.name, expected.name, "name")
    assert_equal(actual.data.email, expected.email, "email")
    assert_equal(actual.status, 201, "status")
    assert_equal(actual.success, True, "success")
    assert_equal(actual.message, "User account created successfully", "message")


@allure.step("Проверка авторизации пользователя")
def assert_login_user(
        actual: UserSchema,
        expected: LoginUserSchema
):
    """
    Проверяет, что данные, возвращённые API после создания/обновления операции, соответствуют ожидаемым.

    :param: actual (UserSchema): Фактические данные операции.
    :param: expected (LoginUserSchema): Ожидаемые данные.
    :raises: AssertionError: Если значения полей не совпадают.
    """
    logger.info("Проверка авторизации пользователя")

    assert_equal(actual.data.name, DataUser.user_name(), "name")
    assert_equal(actual.data.email, expected.email, "email")
    assert_equal(actual.status, 200, "status")
    assert_equal(actual.success, True, "success")
    assert_equal(actual.message, "Login successful", "message")
    assert_equal(actual.data.id, DataUser.user_id(), "id")
