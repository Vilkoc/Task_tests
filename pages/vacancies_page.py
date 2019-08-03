from methods import Methods
from locators import LocatorsVacanvies
from config import EXTRA_LONG_PAUSE


class VacanciesPage(Methods):
    """Sign in page with login method for any type of person"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsVacanvies

    def is_confirmation_sent(self):
        self.pause(EXTRA_LONG_PAUSE)
        text = self.get_text_of_element(self.locators.POP_UP_WINDOW_SIGN_UP_TEXT)
        return text == 'User has been created successfully. Confirm your email and login into site!'

    def click_confirmation_link(self, link):
        self.driver.get(link)

    def is_instructions_sent(self):
        self.pause(EXTRA_LONG_PAUSE)
        text = self.get_text_of_element(self.locators.POP_UP_WINDOW_FORGOT_PASSWORD_TEXT)
        return text == 'Please check mail for further instructions!'

    def click_ok(self):
        self.click_element(self.locators.POP_UP_WINDOW_FORGOT_PASSWORD_BUTTON)
