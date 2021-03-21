from context.driver import driver
from pages.locators import RegisterPageLocators
from pages.page import Page
from selenium.webdriver.common.keys import Keys


class RegisterPage(Page):
    """Object to represent the register page"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = RegisterPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def search(self, search_term):
        element = super().get_element(RegisterPage.SEARCH_BAR)
        element.clear()
        element.send_keys(search_term)
        element.send_keys(Keys.ENTER)

    def verify_search_results(self, url):
        RegisterPage.SEARCH_RESULT.parameterize(url)
        assert super().element_exists(SearchPageLocators.SEARCH_RESULT) is True, (
            "Expected search result was not found on the search page"
        )

    def element_exists(self, element):
        element = getattr(RegisterPageLocators, element)
        assert super().element_exists(element) is True, (
            "Expected element was not found"
        )

    def all_register_element_exists(self):
        for element in [a for a in dir(RegisterPageLocators) if not a.startswith('__') and not callable(getattr(RegisterPageLocators, a))]:
            assert super().element_exists(getattr(RegisterPageLocators, element)) is True, (
                "Expected element was not found"
            )


register_page = RegisterPage.get_instance()
