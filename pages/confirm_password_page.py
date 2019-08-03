from methods import Methods
from locators import LocatorsConfirmPassword


class ConfirmPassword(Methods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsConfirmPassword

    def enter_new_password(self, password):
        self.send_keys(self.locators.NEW_PASSWORD, password)

    def enter_confirm_password(self, password):
        self.send_keys(self.locators.CONFIRMATION_PASSWORD, password)

    def click_register_button(self):
        self.click_element(self.locators.REGISTER_BUTTON)

