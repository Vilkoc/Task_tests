from locators import LocatorsSignIn
from credentials import Credentials


class SignInPage:
    """Sign in page with login method for any type of person"""
    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsSignIn

    def enter_credentials(self, username, passwd):
        """Clears textboxes and enters username and password"""
        self.browser.clear_element(self.locators.EMAIL)
        self.browser.send_keys(self.locators.EMAIL, username)
        self.browser.clear_element(self.locators.PASSWORD)
        self.browser.send_keys(self.locators.PASSWORD, passwd)

    # def click_sign_in(self):
    #     """Clicks 'Sign In' button"""
    #     self.browser.click_element(self.locators.SIGN_IN)

    def login(self, person):
        """Logins any person. It starts from homepage for unlogined person"""
        self.enter_credentials(*Credentials[person])
        self.click_sign_in()

    def enter_sign_in_email(self, email):
        self.browser.send_keys(self.locators.EMAIL_SIGN_IN, email)

    def enter_sign_in_password(self, password):
        self.browser.send_keys(self.locators.PASSWORD_SIGN_IN, password)

    def click_sign_in(self):
        self.browser.click_element(self.locators.BUTTON_SIGN_IN)

    # def login_user(self, username, password):
    #     self.header.click_icon()
    #     self.header.click_log_in()
    #     self.enter_sign_in_email(username)
    #     self.enter_sign_in_password(password)
    #     self.click_sign_in()

    def click_sign_up_tab(self):
        self.browser.click_element_by_text(self.locators.TAB_SIGN_UP, "Sign Up")

    def enter_sign_up_email(self, email):
        self.browser.send_keys(self.locators.EMAIL_SIGN_UP, email)

    def enter_sign_up_password(self, password):
        self.browser.send_keys(self.locators.PASSWORD_SIGN_UP, password)

    def enter_sign_up_matching_password(self, matching_password):
        self.browser.send_keys(self.locators.PASSWORD_MATCHING_SIGN_UP, matching_password)

    def click_sing_up_button(self):
        self.browser.click_element(self.locators.BUTTON_SIGN_UP)

    def click_forgot_password(self):
        self.browser.click_element(self.locators.FORGOT_PASSWORD)

    def is_password_restored(self):
        text = self.browser.get_text_of_element(self.locators.POP_UP_FORGOT_PASSWORD_TEXT)
        return text == 'Password restored successfully! Please sign in.'

    def click_ok(self):
        self.browser.click_element(self.locators.POP_UP_FORGOT_PASSWORD_BUTTON)
