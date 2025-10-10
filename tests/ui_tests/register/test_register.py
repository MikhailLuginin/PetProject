import allure

from configs.config import base_settings
from pages.register_page.register_locators import *
from pages.register_page.register_page import RegisterPage
from tools.assertions.ui_assertions.base import BaseAssertions
from tools.fakers import fakers
from tools.routes import APIRoutes


@allure.parent_suite('UI tests')
@allure.epic('UI tests')
@allure.feature('Тесты на регистрацию')
class TestRegister:

    @allure.title('Проверка успешной регистрации')
    def test_successful_registration(self, clear_context_before_test, page):
        password = fakers.fake_password()
        user_name = fakers.fake_username()
        register_page = RegisterPage(page)
        assertions = BaseAssertions(page)
        with allure.step("Переход на страницу регистрации"):
            register_page.open(f"{base_settings.base_url}{APIRoutes.register}")
        with allure.step("Ввод логина"):
            register_page.input_username(user_name)
        with allure.step("Ввод пароля"):
            register_page.input_password(password)
        with allure.step("Ввод пароля повторно"):
            register_page.input_confirm_password(password)
        with allure.step("Нажатие кнопки создать"):
            register_page.click_confirm_button()
        with allure.step("Проверка url"):
            assertions.check_url(f"{base_settings.base_url}{APIRoutes.login}")
        with allure.step("Проверка сообщения"):
            assertions.have_text(message_loc, "Successfully registered, you can log in now.")

    @allure.title('Проверка регистрации без указания имени пользователя')
    def test_registration_with_missing_username(self, clear_context_before_test, page):
        password = fakers.fake_password()
        register_page = RegisterPage(page)
        assertions = BaseAssertions(page)
        with allure.step("Переход на страницу регистрации"):
            register_page.open(f"{base_settings.base_url}{APIRoutes.register}")
        with allure.step("Ввод пароля"):
            register_page.input_password(password)
        with allure.step("Ввод пароля повторно"):
            register_page.input_confirm_password(password)
        with allure.step("Нажатие кнопки создать"):
            register_page.click_confirm_button()
        with allure.step("Проверка url"):
            assertions.check_url(f"{base_settings.base_url}{APIRoutes.register}")
        with allure.step("Проверка сообщения"):
            assertions.have_text(message_loc, "All fields are required.")

    @allure.title('Проверка регистрации без указания пароля')
    def test_registration_with_missing_password(self, clear_context_before_test, page):
        user_name = fakers.fake_username()
        password = fakers.fake_password()
        register_page = RegisterPage(page)
        assertions = BaseAssertions(page)
        with allure.step("Переход на страницу регистрации"):
            register_page.open(f"{base_settings.base_url}{APIRoutes.register}")
        with allure.step("Ввод логина"):
            register_page.input_username(user_name)
        with allure.step("Ввод пароля"):
            register_page.input_password(password)
        with allure.step("Нажатие кнопки создать"):
            register_page.click_confirm_button()
        with allure.step("Проверка url"):
            assertions.check_url(f"{base_settings.base_url}{APIRoutes.register}")
        with allure.step("Проверка сообщения"):
            assertions.have_text(message_loc, "All fields are required.")

    @allure.title('Проверка регистрации с использованием несовпадающих паролей')
    def test_registration_with_non_matching_passwords(self, clear_context_before_test, page):
        user_name = fakers.fake_username()
        password_1 = fakers.fake_password()
        password_2 = fakers.fake_password()
        register_page = RegisterPage(page)
        assertions = BaseAssertions(page)
        with allure.step("Переход на страницу регистрации"):
            register_page.open(f"{base_settings.base_url}{APIRoutes.register}")
        with allure.step("Ввод логина"):
            register_page.input_username(user_name)
        with allure.step("Ввод пароля"):
            register_page.input_password(password_1)
        with allure.step("Ввод пароля повторно"):
            register_page.input_confirm_password(password_2)
        with allure.step("Нажатие кнопки создать"):
            register_page.click_confirm_button()
        with allure.step("Проверка url"):
            assertions.check_url(f"{base_settings.base_url}{APIRoutes.register}")
        with allure.step("Проверка сообщения"):
            assertions.have_text(message_loc, "Passwords do not match.")
