from methods import Methods
from locators import LocatorsUsers
from pages.home_page import HomePage

class UserProfilePage(Header, Methods):
    """Inherits click_icon method from HomePage"""
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        self.locator_fields = LocatorsUsers

    def click_profile(self):
        self.click_dropdown('Log in')

    def click_logout(self):
        try:
            self.click_dropdown(1)
        except:
            self.click_icon()
            self.click_dropdown(1)

