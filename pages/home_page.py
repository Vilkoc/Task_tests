from methods import Methods
from locators import LocatorsHeader
from pages.header import Header


class HomePage(Header, Methods):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.locators = LocatorsHeader