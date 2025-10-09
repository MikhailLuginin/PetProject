from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.inputs_page.inputs_locators import *


class InputsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def click_button_visible_data(self):
        self.click(locator=button_visible_data_loc)

    def input_integer(self, value):
        self.input(locator=integer_loc, value=value)
