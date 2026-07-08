import os
import time

from playwright.sync_api import sync_playwright


def before_all(context):
    headless_value = os.getenv("PLAYWRIGHT_HEADLESS", "true").lower()
    headless = headless_value not in {"0", "false", "no", "off"}

    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=headless)
    context.page = context.browser.new_page()
    time.sleep(2.0)


def after_all(context):
    time.sleep(1.5)
    if hasattr(context, "page") and context.page is not None:
        context.page.close()
    if hasattr(context, "browser") and context.browser is not None:
        context.browser.close()
    if hasattr(context, "playwright") and context.playwright is not None:
        context.playwright.stop()
