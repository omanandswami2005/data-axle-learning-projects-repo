import time

from playwright.sync_api import Page


class ProfilePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)
        time.sleep(3.0)

    def fill_form(self, name: str, phone: str):
        self.page.locator("xpath=//*[@id='name']").fill(name)
        self.page.locator("xpath=//*[@id='phone']").fill(phone)
        time.sleep(1.0)

    def submit(self):
        self.page.locator("xpath=//button[@type='submit']").click()
        time.sleep(1.5)

    def get_feedback_text(self) -> str:
        time.sleep(1.0)
        return self.page.locator("xpath=//*[@id='feedback']").inner_text()
