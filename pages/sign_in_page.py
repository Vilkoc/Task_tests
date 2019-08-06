from locators import LocatorsSignIn
from credentials import Credentials
from pages.header import Header


class SignInPage():
    """Sign in page with login method for any type of person"""

    def __init__(self, browser):
        self.browser = browser
        self.header = Header(browser)
        self.locators = LocatorsSignIn

    def enter_credentials(self, username, passwd):
        """Clears textboxes and enters username and password"""
        self.browser.clear_element(self.locators.EMAIL)
        self.browser.send_keys(self.locators.EMAIL, username)
        self.browser.clear_element(self.locators.PASSWORD)
        self.browser.send_keys(self.locators.PASSWORD, passwd)

    def click_sign_in(self):
        """Clicks 'Sign In' button"""
        self.browser.click_element(self.locators.SIGN_IN)

    def login(self, person):
        """Logins any person. It starts from homepage for unlogined person"""
        self.header.select_option('Log in')
        self.enter_credentials(*Credentials[person])
        self.click_sign_in()
