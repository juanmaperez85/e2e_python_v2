from behave import given, when, then
from context.config import settings
from context.driver import driver
from pages.page import page
from pages.locators import LoginPage

"""Common hooks for any scenerio"""


@given(u'an internet user')
def fake(context):
    pass


@given(u'a registered client')
@when(u'registered in packlink WITH credentials')
def login_website(context):
    driver.navigate(settings.login_url)
    email = page.get_element(LoginPage.email)
    email.send_keys(settings.user)
    password = page.get_element(LoginPage.password)
    password.send_keys(settings.password)
    page.click_element(LoginPage.button)


@then(u'close session')
def logout(context):
    driver.navigate(settings.logout_url)


@when(u'going to packlink_registro page')
def load_website(context):
    driver.navigate(settings.register_url)

