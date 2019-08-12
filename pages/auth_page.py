from locators import LocatorsSignIn


class AuthPage():
    """ Page for sign in, sign up and forgot password"""

    def __init__(self, base_obj):
        self.browser = base_obj
        self.locators = LocatorsSignIn

    def enter_sign_in_email(self, email):
        self.browser.send_keys(self.locators.EMAIL_SIGN_IN, email)

    def enter_sign_in_password(self, password):
        self.browser.send_keys(self.locators.PASSWORD_SIGN_IN, password)

    def click_sign_in(self):
        self.browser.click_element(self.locators.BUTTON_SIGN_IN)

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
