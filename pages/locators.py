from selenium.webdriver.common.by import By


class Locator:
    """Locator objects for finding Selenium WebElements"""
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)


class RegisterPageLocators:
    """Class for register page selectors"""
    email = Locator(By.XPATH, '//*[@id="email"]')
    password = Locator(By.XPATH, '//*[@id="password"]')
    shipments = Locator(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/section[2]/div/form/fieldset[2]/div[1]')
    ecommerces = Locator(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/section[2]/div/form/fieldset[2]/div[2]')
    marketplace = Locator(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/section[2]/div/form/fieldset[2]/div[3]')
    phone = Locator(By.XPATH, '//*[@id="phone"]')
    terms = Locator(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/section[2]/div/form/fieldset[3]/div[1]/label/input')
    marketing = Locator(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/section[2]/div/form/fieldset[3]/div[2]/label/input')


class LoginPage:
    email = Locator(By.XPATH, '//*[@id="email"]')
    password = Locator(By.XPATH, '//*[@id="password"]')
    button = Locator(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/main/section[2]/div/form/fieldset/button')


class PrivatePageLocators:
    search = Locator(By.XPATH, '//*[@id="shipmentSearch"]')
    newButton = Locator(By.XPATH, '/html/body/div[1]/main-app/div[1]/div[1]/react-component/main/section/div/section/section/section[2]/footer/button')
    cityFrom = Locator(By.XPATH, '(//*[@type="search"])[2]')
    cityFromSuggestion = Locator(By.XPATH, '(//country-postal-code-selector/packlink-selector[2]/div/ul/li[1])[1]')
    cityTo = Locator(By.XPATH, '(//*[@type="search"])[4]')
    cityToSuggestion = Locator(By.XPATH, '(//country-postal-code-selector/packlink-selector[2]/div/ul/li[1])[2]')
    getServicesButton = Locator(By.XPATH, '//create-info/section/form/div/div/button')
    setFirstService = Locator(By.XPATH, '//article[1]/div/section[6]/button')
    weight = Locator(By.XPATH, '//*[@id="weight-0"]')
    lenght = Locator(By.XPATH, '//*[@id="length-0"]')
    width = Locator(By.XPATH, '//*[@id="width-0"]')
    height = Locator(By.XPATH, '//*[@id="height-0"]')
    saveButtom = Locator(By.XPATH, '//shipment-sidebar/div/section[1]/react-component[2]/button')
    draftMenu = Locator(By.XPATH, '/html/body/div[1]/main-app/div[1]/div[1]/react-component/main/aside/ul/li[5]')
    firstService = Locator(By.XPATH, '(//main/section/div/div/div)[1]')
    draftMenuFirstCheckbox = Locator(By.XPATH, '(//div/label/span[1])[3]')
