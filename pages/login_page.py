import time

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)
        time.sleep(3.0)

    def enter_email(self, email: str):
        self.page.locator("xpath=//*[@id='email']").fill(email)
        time.sleep(1.0)

    def enter_password(self, password: str):
        self.page.locator("xpath=//*[@id='password']").fill(password)
        time.sleep(1.0)

    def submit(self):
        self.page.locator("xpath=//button[@type='submit']").click()
        time.sleep(1.5)

    def get_feedback_text(self) -> str:
        time.sleep(1.0)
        return self.page.locator("xpath=//*[@id='feedback']").inner_text()
