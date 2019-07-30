from methods import Methods
from locators import LocatorsHeader

class Header():
    """Header page, which will be inherited by other pages"""
    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)
        self.locators = LocatorsHeader

    def click_icon(self):
        """Clicks on the round icon"""
        self.methods.click_element(self.locators.ICON)

    def select_option(self, pick_item):
        """The pick_item is default string parameter which accepts only 'Log in', 'Profile', 'Log out' values"""
        values = ('Log in', 'Profile', 'Log out')
        if pick_item not in values:
            raise Exception('Incorrect value for click_dropdown function')
        self.methods.click_element_by_text(self.locators.DROPDOWN, pick_item)