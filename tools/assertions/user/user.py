import os

import allure
from schemas.user.user_schemas import *
from tools.assertions.base import assert_equal
from tools.constants import Constants
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
        expected: LoginUserSchema,
        user_name,
        user_id
):
    """
    Проверяет, что данные, возвращённые API после авторизации юзера, соответствуют ожидаемым.

    :param: actual (UserSchema): Фактические данные юзера.
    :param: expected (LoginUserSchema): Ожидаемые данные.
    :raises: AssertionError: Если значения полей не совпадают.
    """
    logger.info("Проверка авторизации пользователя")
    assert_equal(actual.data.name, user_name, "name")
    assert_equal(actual.data.email, expected.email, "email")
    assert_equal(actual.status, 200, "status")
    assert_equal(actual.success, True, "success")
    assert_equal(actual.message, "Login successful", "message")
    assert_equal(actual.data.id, user_id, "id")


@allure.step("Проверка изменения данных пользователя")
def assert_update_user(
        actual: UserSchema,
        expected: UpdateUserSchema
):
    """
    Проверяет, что данные, возвращённые API после изменения юзера, соответствуют ожидаемым.

    :param: actual (UserSchema): Фактические данные юзера.
    :param: expected (UpdateUserSchema): Ожидаемые данные.
    :raises: AssertionError: Если значения полей не совпадают.
    """
    logger.info("Проверка авторизации пользователя")

    assert_equal(actual.data.name, expected.name, "name")
    assert_equal(actual.data.email, Constants.email, "email")
    assert_equal(actual.status, 200, "status")
    assert_equal(actual.success, True, "success")
    assert_equal(actual.message, "Profile updated successful", "message")
    assert_equal(actual.data.id,  Constants.user_id, "id")
    assert_equal(actual.data.phone, expected.phone, "phone")
    assert_equal(actual.data.company, expected.company, "company")
