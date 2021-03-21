from context.config import settings
from context.driver import driver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


class Page:
    """Base class for all page objects in the Page Object Model"""
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Page()
        return cls.instance

    def __init__(self):
        self.driver = driver.get_driver()
        super().__init__()

    def _execute_with_wait(self, condition):
        return WebDriverWait(self.driver, settings.driver_timeout).until(condition)

    def element_exists(self, locator):
        try:
            self._execute_with_wait(
                ec.presence_of_element_located(
                    (locator.l_type, locator.selector))
            )
            return True
        except TimeoutException:
            return False

    def get_element(self, locator):
        if not self.element_exists(locator):
            raise NoSuchElementException("Could not find {locator.selector}")

        return self.driver.find_element(locator.l_type, locator.selector)

    def click_element(self, locator):
        self.driver.find_element(locator.l_type, locator.selector).click()


page = Page.get_instance()
