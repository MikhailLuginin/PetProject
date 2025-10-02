import allure

from configs.config import base_settings
from pages.register_page.register_page import RegisterPage
from tools.fakers import fakers
from tools.routes import APIRoutes


@allure.parent_suite('API tests')
@allure.epic('API tests')
@allure.feature('Тесты на юзера')
class TestRegister:

    @allure.title('Проверка успешной регистрации')
    def test_successful_registration(self, page):
        password = fakers.fake_password()
        user_name = fakers.fake_username()
        register_page = RegisterPage(page)
        register_page.open(f"{base_settings.base_url}{APIRoutes.register}")
        register_page.input_username(user_name)
        register_page.input_password(password)
        register_page.input_confirm_password(password)
        register_page.click_confirm_button()
        assert register_page.get_url() == f"{base_settings.base_url}{APIRoutes.login}"
        assert register_page.get_message() == "Successfully registered, you can log in now."

    @allure.title('Проверка регистрации без указания имени пользователя')
    def test_registration_with_missing_username(self, page):
        password = fakers.fake_password()
        register_page = RegisterPage(page)
        register_page.open(f"{base_settings.base_url}{APIRoutes.register}")
        register_page.input_password(password)
        register_page.input_confirm_password(password)
        register_page.click_confirm_button()
        assert register_page.get_url() == f"{base_settings.base_url}{APIRoutes.register}"
        assert register_page.get_message() == "All fields are required."

    @allure.title('Проверка регистрации без указания пароля')
    def test_registration_with_missing_password(self, page):
        password = fakers.fake_password()
        register_page = RegisterPage(page)
        register_page.open(f"{base_settings.base_url}{APIRoutes.register}")
        register_page.input_username(fakers.fake_username())
        register_page.input_confirm_password(password)
        register_page.click_confirm_button()
        assert register_page.get_url() == f"{base_settings.base_url}{APIRoutes.register}"
        assert register_page.get_message() == "All fields are required."

    @allure.title('Проверка регистрации с использованием несовпадающих паролей')
    def test_registration_with_non_matching_passwords(self, page):
        register_page = RegisterPage(page)
        register_page.open(f"{base_settings.base_url}{APIRoutes.register}")
        register_page.input_username(fakers.fake_username())
        register_page.input_password(fakers.fake_password())
        register_page.input_confirm_password(fakers.fake_password())
        register_page.click_confirm_button()
        assert register_page.get_url() == f"{base_settings.base_url}{APIRoutes.register}"
        assert register_page.get_message() == "Passwords do not match."
