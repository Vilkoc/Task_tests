from methods import Methods
from locators import LocatorsSignIn
from credentials import Credentials


class SignInPage(Methods):
    """Sign in page with login method for any type of person"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsSignIn

    def clear_boxes(self):
        self.clear_element(self.locators.EMAIL)
        self.clear_element(self.locators.PASSWORD)

    def enter_credentials(self, username, passwd):
        self.send_keys(self.locators.EMAIL, username)
        self.send_keys(self.locators.PASSWORD, passwd)

    def click_sign_in(self):
        self.click_element(self.locators.SIGN_IN)

    def login(self, person):
        self.clear_boxes()
        self.enter_credentials(*Credentials[person])
        self.click_sign_in()

