from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.login_page.login_locators import *


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def get_username(self):
        return self.get_text(default_username_loc)

    def input_username(self, value):
        self.input(locator=username_loc, value=value)

    def get_password(self):
        return self.get_text(default_password_loc)

    def input_password(self, value):
        self.input(locator=password_loc, value=value)

    def click_login_button(self):
        self.click(login_button_loc)
