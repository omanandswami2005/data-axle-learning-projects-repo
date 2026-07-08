import time

from behave import given, when, then

from pages.search_page import SearchPage


@given("the search page is available")
def step_given_search_page_available(context):
    context.base_url = "http://127.0.0.1:8000/app/pages/search.html"


@when("the user opens the search page")
def step_when_user_opens_search_page(context):
    time.sleep(1.0)
    context.current_page = SearchPage(context.page)
    context.current_page.open(context.base_url)


@when('the user searches for "{term}"')
def step_when_user_searches_for(context, term):
    context.current_page.enter_search_term(term)
    context.current_page.click_search()


@then('the search results should include "{expected_text}"')
def step_then_search_results_should_include(context, expected_text):
    actual_text = context.current_page.get_result_text()
    assert expected_text in actual_text, (
        f"Expected '{expected_text}' in '{actual_text}'"
    )
