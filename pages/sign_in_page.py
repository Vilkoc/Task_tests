from locators import LocatorsSignIn
from credentials import Credentials


class SignInPage():
    """Sign in page with login method for any type of person"""

    def __init__(self, base_obj):
        self.header = base_obj.header
        self.browser = base_obj.browser

        self.locators = LocatorsSignIn

    def clear_boxes(self):
        self.browser.clear_element(self.locators.EMAIL)
        self.browser.clear_element(self.locators.PASSWORD)

    def enter_credentials(self, username, passwd):
        self.browser.send_keys(self.locators.EMAIL, username)
        self.browser.send_keys(self.locators.PASSWORD, passwd)

    def click_sign_in(self):
        self.browser.click_element(self.locators.SIGN_IN)

    def login(self, person):
        self.header.select_option('Log in')
        self.clear_boxes()
        self.enter_credentials(*Credentials[person])
        self.click_sign_in()