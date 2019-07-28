from methods import Methods
from locators import Locators

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)
        self.locators = Locators


    def click_icon(self):
        self.methods.click_element(self.locators.ICON)

    def click_login(self):
        self.methods.click_element(self.locators.LOGIN)

