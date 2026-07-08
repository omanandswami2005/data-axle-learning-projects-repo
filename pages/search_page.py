import time

from playwright.sync_api import Page


class SearchPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)
        time.sleep(3.0)

    def enter_search_term(self, term: str):
        self.page.locator("xpath=//*[@id='search']").fill(term)
        time.sleep(1.0)

    def click_search(self):
        self.page.locator("xpath=//button").click()
        time.sleep(1.5)

    def get_result_text(self) -> str:
        time.sleep(1.0)
        return self.page.locator("xpath=//*[@id='result']").inner_text()
