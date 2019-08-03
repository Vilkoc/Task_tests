from methods import Methods
from locators import LocatorsForgotPassword


class ForgotPasswordPage(Methods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsForgotPassword

    def enter_login_email(self, email):
        self.send_keys(self.locators.EMAIL, email)

    def click_submit_button(self):
        self.click_element(self.locators.SUBMIT_BUTTON)

