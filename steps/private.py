import time
from behave import given, when, then, step
from context.driver import driver
from context.config import settings
from pages.private import private_page
from pages.page import page
from pages.locators import PrivatePageLocators

"""Hooks for interacting with private page"""


@Then(u'it will land into the platform dashboard')
def in_private(context):
    private_page.element_exists('search')


@When(u'create a order : "{fromCity}" "{toCity}" "{weight}" kg "{lenght}"cm x "{width}" cm x "{height}" cm')
def create(context, fromCity, toCity, weight, lenght, width, height):
    driver.navigate(settings.create_url)
    page.get_element(PrivatePageLocators.cityFrom).send_keys(fromCity)
    time.sleep(1)
    page.click_element(PrivatePageLocators.cityFromSuggestion)
    page.get_element(PrivatePageLocators.cityTo).send_keys(toCity)
    time.sleep(1)
    page.click_element(PrivatePageLocators.cityToSuggestion)
    page.get_element(PrivatePageLocators.weight).send_keys(weight)
    page.get_element(PrivatePageLocators.lenght).send_keys(lenght)
    page.get_element(PrivatePageLocators.width).send_keys(width)
    page.get_element(PrivatePageLocators.height).send_keys(height)


@Then('it will select the first service of the list')
def select_first_draft(context):
    page.click_element(PrivatePageLocators.getServicesButton)
    time.sleep(1)
    page.click_element(PrivatePageLocators.setFirstService)
    page.click_element(PrivatePageLocators.saveButtom)


@When(u'a service has been selected')
def select_first_service_draft(context):
    driver.navigate(settings.draft_url)
    time.sleep(1)


@Then(u'it will save the shipment as a draft')
def check_service_as_draft(context):
    page.element_exists(PrivatePageLocators.firstService)


@step(u'it will appear in the shipment list')
def check_service_shipment_list(context):
    driver.navigate(settings.shipment_url)
    page.element_exists(PrivatePageLocators.firstService)
