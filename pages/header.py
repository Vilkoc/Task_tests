from methods import Methods
from locators import Locators

class Header():
    """This is parent class"""
    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)
        self.locators = Locators

    def click_icon(self):
        """Clicks on the round icon"""
        self.methods.click_element(self.locators.ICON)

    def click_dropdown(self, pick_item):
        """The pick_item is default string parameter which accepts only 'Log in', 'Profile', 'Log out' values"""
        values = ('Log in', 'Profile', 'Log out')
        if pick_item not in values:
            raise Exception('Incorrect value for click_dropdown function')
        self.methods.click_element_by_text(self.locators.DROPDOWN, pick_item)