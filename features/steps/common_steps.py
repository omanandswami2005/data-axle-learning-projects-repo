import time

from behave import given, when, then

from pages.home_page import HomePage


@given("the sample app is available")
def step_given_sample_app_available(context):
    context.base_url = "http://127.0.0.1:8000/app/index.html"


@when("the user opens the homepage")
def step_when_user_opens_homepage(context):
    time.sleep(1.0)
    context.home_page = HomePage(context.page)
    context.home_page.open(context.base_url)


@then('the page heading should be "{expected_heading}"')
def step_then_page_heading_should_be(context, expected_heading):
    time.sleep(1.0)
    actual_heading = context.home_page.get_heading_text()
    assert actual_heading == expected_heading, (
        f"Expected heading '{expected_heading}', but got '{actual_heading}'"
    )


@then('the page should display the text "{expected_text}"')
def step_then_page_should_display_text(context, expected_text):
    time.sleep(1.0)
    actual_text = context.home_page.get_page_text()
    assert expected_text in actual_text, (
        f"Expected text '{expected_text}' to be present, but got '{actual_text}'"
    )
