from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.register_page.register_locators import RegisterLocators


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def input_username(self, value):
        self.input(locator=RegisterLocators.username, value=value)

    def input_password(self, value):
        self.input(locator=RegisterLocators.password, value=value)

    def input_confirm_password(self, value):
        self.input(locator=RegisterLocators.confirm_password, value=value)

    def click_confirm_button(self):
        self.click(locator=RegisterLocators.confirm_button)
