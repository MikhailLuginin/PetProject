from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.login_page.login_locators import LoginLocators


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def get_username(self):
        return self.get_text(LoginLocators.default_username)

    def input_username(self, value):
        self.input(locator=LoginLocators.username, value=value)

    def get_password(self):
        return self.get_text(LoginLocators.default_password)

    def input_password(self, value):
        self.input(locator=LoginLocators.password, value=value)

    def click_login_button(self):
        self.click(LoginLocators.login_button)
