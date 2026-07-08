from behave import given, then, when
from playwright.sync_api import expect


BASE_URL = "https://the-internet.herokuapp.com"


@given("I open the dropdown page")
def open_dropdown_page(context):
    context.page.goto(f"{BASE_URL}/dropdown")
    expect(context.page.locator("xpath=//h3")).to_have_text("Dropdown List")


@when('I select "{option_text}" from the dropdown')
def select_dropdown_option(context, option_text):
    context.page.locator("xpath=//select[@id='dropdown']").select_option(
        label=option_text
    )


@then('the dropdown value should be "{expected_value}"')
def check_dropdown_value(context, expected_value):
    dropdown = context.page.locator("xpath=//select[@id='dropdown']")
    expect(dropdown).to_have_value(expected_value)
