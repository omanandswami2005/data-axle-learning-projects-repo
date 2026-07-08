import time

from behave import given, when, then

from pages.checkout_page import CheckoutPage


@given("the checkout page is available")
def step_given_checkout_page_available(context):
    context.base_url = "http://127.0.0.1:8000/app/pages/checkout.html"


@when("the user opens the checkout page")
def step_when_user_opens_checkout_page(context):
    time.sleep(1.0)
    context.current_page = CheckoutPage(context.page)
    context.current_page.open(context.base_url)


@when('the user enters the shipping details for "{name}"')
def step_when_user_enters_shipping_details(context, name):
    context.current_page.fill_form(name, "123 Main St", "Springfield")


@when("the user confirms the order")
def step_when_user_confirms_order(context):
    context.current_page.submit()


@then('the confirmation message should contain "{expected_text}"')
def step_then_confirmation_message_should_contain(context, expected_text):
    actual_text = context.current_page.get_feedback_text()
    assert expected_text in actual_text, (
        f"Expected '{expected_text}' in '{actual_text}'"
    )
