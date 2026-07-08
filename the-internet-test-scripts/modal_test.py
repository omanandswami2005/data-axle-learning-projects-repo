import os

from playwright.sync_api import TimeoutError, expect, sync_playwright


BASE_URL = "https://the-internet.herokuapp.com"


def is_headless() -> bool:
    return os.getenv("HEADLESS", "false").lower() == "true"


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=is_headless(), slow_mo=300)
        context = browser.new_context()
        page = context.new_page()

        page.goto(f"{BASE_URL}/entry_ad")
        expect(page.locator("xpath=//h3").first).to_have_text("Entry Ad")

        modal = page.locator("xpath=//div[@id='modal']")

        try:
            expect(modal).to_be_visible(timeout=5000)
        except TimeoutError:
            page.locator("xpath=//a[normalize-space()='click here']").click()
            page.reload()
            expect(modal).to_be_visible(timeout=5000)

        expect(page.locator("xpath=//div[contains(@class, 'modal-title')]//h3")).to_have_text(
            "This is a modal window"
        )
        page.locator("xpath=//div[contains(@class, 'modal-footer')]//p[normalize-space()='Close']").click()
        expect(modal).to_be_hidden()

        print("Modal test passed: entry modal opened and was closed.")
        browser.close()


if __name__ == "__main__":
    main()
