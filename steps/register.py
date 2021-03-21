from behave import given, when, then
from pages.register import register_page

"""Hooks for interacting with register page"""


@when(u'I search for "{search_term}"')
def search(context, search_term):
    search_page.search(search_term)


@then(u'I should see "{url}" in the results')
def results(context, url):
    search_page.verify_search_results(url)


@then('the "{element}" element is displayed')
def check_element(context, element):
    register_page.element_exists(element)


@then('it will see the registration form with required fields')
def check_element(context):
    register_page.all_register_element_exists()
