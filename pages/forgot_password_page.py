from locators import LocatorsForgotPassword


class ForgotPasswordPage:
    """ Page for renew password"""

    def __init__(self, base_obj):
        self.browser = base_obj
        self.locators = LocatorsForgotPassword

    def enter_login_email(self, email):
        self.browser.send_keys(self.locators.EMAIL, email)

    def click_submit_button(self):
        self.browser.click_element(self.locators.SUBMIT_BUTTON)
