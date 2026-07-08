import os

from playwright.sync_api import expect, sync_playwright


BASE_URL = "https://the-internet.herokuapp.com"


def is_headless() -> bool:
    return os.getenv("HEADLESS", "false").lower() == "true"


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=is_headless(), slow_mo=300)
        page = browser.new_page()

        page.goto(f"{BASE_URL}/dropdown")
        expect(page.locator("xpath=//h3")).to_have_text("Dropdown List")

        dropdown = page.locator("xpath=//select[@id='dropdown']")
        dropdown.select_option(label="Option 1")
        expect(dropdown).to_have_value("1")

        dropdown.select_option(label="Option 2")
        expect(dropdown).to_have_value("2")

        print("Dropdown test passed: Option 1 and Option 2 were selected.")
        browser.close()


if __name__ == "__main__":
    main()
