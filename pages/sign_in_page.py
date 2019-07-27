from methods import Methods
from locators import Locators
from pages.home_page import HomePage

class SignInPage(HomePage):
    """Inherits click_icon method from HomePage"""
    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)
        self.locators = Locators

    def clear_box(self, box_name):
        self.methods.clear_element('id', self.locators.ID_LOC[box_name])

    def send_keys(self, box_name, keys):
        self.methods.send_keys('id', self.locators.ID_LOC[box_name], keys)

    def click_sign_in(self):
        self.methods.click_element('css', self.locators.SIGN_IN, wait_id='VISIBLE')

    def click_logout(self):
        self.click_icon()
        self.methods.click_element('css', self.locators.DROPDOWN, numb_list=1, wait_id='VISIBLE')