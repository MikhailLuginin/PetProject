from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.register_page.register_locators import *


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def input_username(self, value):
        self.input(locator=username_loc, value=value)

    def input_password(self, value):
        self.input(locator=password_loc, value=value)

    def input_confirm_password(self, value):
        self.input(locator=confirm_password_loc, value=value)

    def click_confirm_button(self):
        self.click(locator=confirm_button_loc)
