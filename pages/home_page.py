from methods import Methods
from locators import Locators
from pages.header import Header

class HomePage(Header):

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)
        self.locators = Locators

