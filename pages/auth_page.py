from methods import Methods
from locators import LocatorsSignIn
from credentials import Credentials
from pages.header import Header


class AuthPage(Methods):
    """Sign in page with login method for any type of person"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsSignIn

    def clear_boxes(self):
        self.clear_element(self.locators.EMAIL_SIGN_IN)
        self.clear_element(self.locators.PASSWORD_SIGN_IN)

    def enter_sign_in_email(self, email):
        self.send_keys(self.locators.EMAIL_SIGN_IN, email)

    def enter_sign_in_password(self, password):
        self.send_keys(self.locators.PASSWORD_SIGN_IN, password)

    def enter_credentials(self, username, password):
        self.enter_sign_in_email(username)
        self.enter_sign_in_password(password)

    def click_sign_in(self):
        self.click_element(self.locators.BUTTON_SIGN_IN)

    def login(self, person):
        self.clear_boxes()
        self.enter_credentials(*Credentials[person])
        self.click_sign_in()

    def login_user(self,username, password):
        header = Header(self.driver)
        header.click_icon()
        header.click_log_in()
        self.enter_sign_in_email(username)
        self.enter_sign_in_password(password)
        self.click_sign_in()

    def click_sign_up_tab(self):
        self.click_element_by_text_simple(self.locators.TAB_SIGN_UP)

    def enter_sign_up_email(self, email):
        self.send_keys(self.locators.EMAIL_SIGN_UP, email)

    def enter_sign_up_password(self, password):
        self.send_keys(self.locators.PASSWORD_SIGN_UP, password)

    def enter_sign_up_matching_password(self, matching_password):
        self.send_keys(self.locators.PASSWORD_MATCHING_SIGN_UP, matching_password)

    def click_sing_up_button(self):
        self.click_element(self.locators.BUTTON_SIGN_UP)

    def click_forgot_password(self):
        self.click_element(self.locators.FORGOT_PASSWORD)

    def is_password_restored(self):
        text = self.get_text_of_element(self.locators.POP_UP_FORGOT_PASSWORD_TEXT)
        return text == 'Password restored successfully! Please sign in.'

    def click_ok(self):
        self.click_element(self.locators.POP_UP_FORGOT_PASSWORD_BUTTON)


