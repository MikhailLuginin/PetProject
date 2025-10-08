import allure

from configs.config import base_settings
from pages.login_page.login_locators import LoginLocators
from pages.login_page.login_page import LoginPage
from tools.assertions.ui_assertions.base import BaseAssertions
from tools.fakers import fakers
from tools.routes import APIRoutes


@allure.parent_suite('UI tests')
@allure.epic('UI tests')
@allure.feature('Тесты на авторизацию')
class TestLogin:

    @allure.title('Проверка успешного входа в систему')
    def test_successful_login(self, clear_context_before_test, page):
        login_page = LoginPage(page)
        assertions = BaseAssertions(page)
        with allure.step("Переход на страницу авторизации"):
            login_page.open(f"{base_settings.base_url}{APIRoutes.login}")
        with allure.step("Получение логина"):
            username = login_page.get_username()
        with allure.step("Получение пароля"):
            password = login_page.get_password()
        with allure.step("Ввод логина"):
            login_page.input_username(username)
        with allure.step("Ввод пароля"):
            login_page.input_password(password)
        with allure.step("Нажатие кнопки вход"):
            login_page.click_login_button()
        with allure.step("Проверка url"):
            assertions.check_url(f"{base_settings.base_url}{APIRoutes.secure}")
        with allure.step("Проверка сообщения"):
            assertions.have_text(LoginLocators.message, "You logged into a secure area!")

    @allure.title('Проверка недопустимого имени пользователя')
    def test_invalid_username(self, clear_context_before_test, page):
        login_page = LoginPage(page)
        assertions = BaseAssertions(page)
        username = fakers.fake_username()
        with allure.step("Переход на страницу авторизации"):
            login_page.open(f"{base_settings.base_url}{APIRoutes.login}")
        with allure.step("Получение пароля"):
            password = login_page.get_password()
        with allure.step("Ввод логина"):
            login_page.input_username(username)
        with allure.step("Ввод пароля"):
            login_page.input_password(password)
        with allure.step("Нажатие кнопки вход"):
            login_page.click_login_button()
        with allure.step("Проверка url"):
            assertions.check_url(f"{base_settings.base_url}{APIRoutes.login}")
        with allure.step("Проверка сообщения"):
            assertions.have_text(LoginLocators.message, "Your username is invalid!")

    @allure.title('Проверка недопустимого пароля пользователя')
    def test_invalid_password(self, clear_context_before_test, page):
        login_page = LoginPage(page)
        assertions = BaseAssertions(page)
        password = fakers.fake_password()
        with allure.step("Переход на страницу авторизации"):
            login_page.open(f"{base_settings.base_url}{APIRoutes.login}")
        with allure.step("Получение логина"):
            username = login_page.get_username()
        with allure.step("Ввод логина"):
            login_page.input_username(username)
        with allure.step("Ввод пароля"):
            login_page.input_password(password)
        with allure.step("Нажатие кнопки вход"):
            login_page.click_login_button()
        with allure.step("Проверка url"):
            assertions.check_url(f"{base_settings.base_url}{APIRoutes.login}")
        with allure.step("Проверка сообщения"):
            assertions.have_text(LoginLocators.message, "Your password is invalid!")
