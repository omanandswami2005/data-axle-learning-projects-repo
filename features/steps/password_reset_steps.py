import time

from behave import given, step_matcher, then, when

from pages.password_reset_page import PasswordResetPage

step_matcher("re")


@given("the password reset page is available")
def step_given_password_reset_page_available(context):
    context.base_url = "http://127.0.0.1:8000/app/pages/password-reset.html"


@when("the user opens the password reset page")
def step_when_user_opens_password_reset_page(context):
    time.sleep(1.0)
    context.current_page = PasswordResetPage(context.page)
    context.current_page.open(context.base_url)


@when(r'the user submits the password reset form for "(.*)"')
def step_when_user_submits_password_reset_form(context, email):
    context.current_page.enter_email(email)
    context.current_page.submit()


@then(r'the reset status should contain "(.*)"')
def step_then_reset_status_should_contain(context, expected_text):
    actual_text = context.current_page.get_feedback_text()
    assert expected_text in actual_text, (
        f"Expected '{expected_text}' in '{actual_text}'"
    )
