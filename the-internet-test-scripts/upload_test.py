from pathlib import Path
import os

from playwright.sync_api import expect, sync_playwright


BASE_URL = "https://the-internet.herokuapp.com"
SCRIPT_DIR = Path(__file__).resolve().parent
UPLOAD_FILE = SCRIPT_DIR / "upload_sample.txt"


def is_headless() -> bool:
    return os.getenv("HEADLESS", "false").lower() == "true"


def main() -> None:
    assert UPLOAD_FILE.exists(), f"Upload file is missing: {UPLOAD_FILE}"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=is_headless(), slow_mo=300)
        page = browser.new_page()

        page.goto(f"{BASE_URL}/upload")
        expect(page.locator("xpath=//h3")).to_have_text("File Uploader")

        page.locator("xpath=//input[@id='file-upload']").set_input_files(str(UPLOAD_FILE))
        page.locator("xpath=//input[@id='file-submit']").click()

        expect(page.locator("xpath=//h3")).to_have_text("File Uploaded!")
        expect(page.locator("xpath=//div[@id='uploaded-files']")).to_have_text(UPLOAD_FILE.name)

        print(f"Upload test passed: {UPLOAD_FILE.name} was uploaded.")
        browser.close()


if __name__ == "__main__":
    main()
