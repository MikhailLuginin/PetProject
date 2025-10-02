import allure

from configs.config import base_settings
from pages.login_page.login_page import LoginPage
from tools.fakers import fakers
from tools.routes import APIRoutes


@allure.parent_suite('UI tests')
@allure.epic('UI tests')
@allure.feature('Тесты на авторизацию')
class TestLogin:

    @allure.title('Проверка успешного входа в систему')
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        login_page.open(f"{base_settings.base_url}{APIRoutes.login}")
        username = login_page.get_username()
        password = login_page.get_password()
        login_page.input_username(username)
        login_page.input_password(password)
        login_page.click_login_button()
        assert login_page.get_url() == f"{base_settings.base_url}{APIRoutes.secure}"
        assert login_page.get_message() == "You logged into a secure area!"

    @allure.title('Проверка недопустимого имени пользователя')
    def test_invalid_username(self, page):
        login_page = LoginPage(page)
        login_page.open(f"{base_settings.base_url}{APIRoutes.login}")
        username = fakers.fake_username()
        password = login_page.get_password()
        login_page.input_username(username)
        login_page.input_password(password)
        login_page.click_login_button()
        assert login_page.get_url() == f"{base_settings.base_url}{APIRoutes.login}"
        assert login_page.get_message() == "Your username is invalid!"

    @allure.title('Проверка недопустимого пароля пользователя')
    def test_invalid_password(self, page):
        login_page = LoginPage(page)
        login_page.open(f"{base_settings.base_url}{APIRoutes.login}")
        username = login_page.get_username()
        password = fakers.fake_password()
        login_page.input_username(username)
        login_page.input_password(password)
        login_page.click_login_button()
        assert login_page.get_url() == f"{base_settings.base_url}{APIRoutes.login}"
        assert login_page.get_message() == "Your password is invalid!"
