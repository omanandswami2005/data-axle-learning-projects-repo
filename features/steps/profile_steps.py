import time

from behave import given, when, then

from pages.profile_page import ProfilePage


@given("the profile page is available")
def step_given_profile_page_available(context):
    context.base_url = "http://127.0.0.1:8000/app/pages/profile.html"


@when("the user opens the profile page")
def step_when_user_opens_profile_page(context):
    time.sleep(1.0)
    context.current_page = ProfilePage(context.page)
    context.current_page.open(context.base_url)


@when('the user updates the profile name to "{name}"')
def step_when_user_updates_profile_name(context, name):
    context.current_page.fill_form(name, "555-1234")
    context.current_page.submit()


@then('the profile summary should contain "{expected_text}"')
def step_then_profile_summary_should_contain(context, expected_text):
    actual_text = context.current_page.get_feedback_text()
    assert expected_text in actual_text, (
        f"Expected '{expected_text}' in '{actual_text}'"
    )
