from methods import Methods
from locators import Locators
from pages.home_page import HomePage


class SignInPage():
    """Inherits click_icon method from HomePage"""
    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)
        self.locators = Locators

    def clear_boxes(self):
        self.methods.clear_element(self.locators.EMAIL)
        self.methods.clear_element(self.locators.PASSWORD)

    def enter_credentials(self, entry):
        (email, passwd) = entry
        self.methods.send_keys(self.locators.EMAIL, email)
        self.methods.send_keys(self.locators.PASSWORD, passwd)

    def click_sign_in(self):
        self.methods.click_element(self.locators.SIGN_IN, wait_id='VISIBLE')

