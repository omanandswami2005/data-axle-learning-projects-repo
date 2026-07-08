import time

from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)
        time.sleep(3.0)

    def get_heading_text(self) -> str:
        time.sleep(1.5)
        return self.page.locator("h1").inner_text()

    def get_page_text(self) -> str:
        time.sleep(1.5)
        return self.page.locator("body").inner_text()
