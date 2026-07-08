import time

from behave import given, step_matcher, then, when

from pages.login_page import LoginPage

step_matcher("re")


@given("the login page is available")
def step_given_login_page_available(context):
    context.base_url = "http://127.0.0.1:8000/app/pages/login.html"


@when("the user opens the login page")
def step_when_user_opens_login_page(context):
    time.sleep(1.0)
    context.current_page = LoginPage(context.page)
    context.current_page.open(context.base_url)


@when(r'the user enters "(.*)" and "(.*)"')
def step_when_user_enters_credentials(context, email, password):
    context.current_page.enter_email(email)
    context.current_page.enter_password(password)


@when("the user submits the login form")
def step_when_user_submits_login_form(context):
    context.current_page.submit()


@then(r'the login feedback should contain "(.*)"')
def step_then_login_feedback_should_contain(context, expected_text):
    actual_text = context.current_page.get_feedback_text()
    assert expected_text in actual_text, (
        f"Expected '{expected_text}' in '{actual_text}'"
    )
