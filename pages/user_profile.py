from methods import Methods
from locators import Locators
from pages.home_page import HomePage

class UserProfilePage(HomePage):
    """Inherits click_icon method from HomePage"""
    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)
        self.locators = Locators

    def click_profile(self):
        self.click_dropdown(0)

    def click_logout(self):
        try:
            self.click_dropdown(1)
        except:
            self.click_icon()
            self.click_dropdown(1)