from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url):
        self.page.goto(url=url, wait_until="domcontentloaded")

    def input(self, locator, value):
        self.page.locator(locator).fill(value)

    def click(self, locator):
        self.page.locator(locator).click()

    def get_url(self):
        return self.page.url

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()
