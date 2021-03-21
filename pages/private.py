from context.driver import driver
from pages.locators import PrivatePageLocators
from pages.page import Page
from selenium.webdriver.common.keys import Keys


class PrivatePage(Page):
    """Object to represent the private dashboard"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = PrivatePage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def element_exists(self, element):
        element = getattr(PrivatePageLocators, element)
        assert super().element_exists(element) is True, (
            "Expected element was not found"
        )


private_page = PrivatePage.get_instance()
