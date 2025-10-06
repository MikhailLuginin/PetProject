from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class BaseAssertions(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def check_url(self, url):
        expect(self.page).to_have_url(url, timeout=5000)

    def check_present(self, locator):
        locator = self.page.locator(locator)
        expect(locator).to_be_visible(visible=True, timeout=5000)

    def check_absence(self, locator):
        locator = self.page.locator(locator)
        expect(locator).to_be_hidden(timeout=5000)

    def have_text(self, locator, text: str):
        locator = self.page.locator(locator)
        expect(locator).to_have_text(text)
