from pathlib import Path
import os

from playwright.sync_api import expect, sync_playwright


BASE_URL = "https://the-internet.herokuapp.com"
SCRIPT_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = SCRIPT_DIR / "downloads"


def is_headless() -> bool:
    return os.getenv("HEADLESS", "false").lower() == "true"


def main() -> None:
    DOWNLOAD_DIR.mkdir(exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=is_headless(), slow_mo=2000)
        page = browser.new_page(accept_downloads=True)

        page.goto(f"{BASE_URL}/download")
        expect(page.locator("xpath=//h3")).to_have_text("File Downloader")

        first_file_link = page.locator("xpath=//div[contains(@class, 'example')]//a").first
        file_name = first_file_link.inner_text()

        with page.expect_download() as download_info:
            first_file_link.click()

        download = download_info.value
        saved_path = DOWNLOAD_DIR / download.suggested_filename
        download.save_as(saved_path)

        assert saved_path.exists(), f"Download was not saved: {saved_path}"
        print(f"Downloaded '{file_name}' to: {saved_path}")

        browser.close()


if __name__ == "__main__":
    main()
