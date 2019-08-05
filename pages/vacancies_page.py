from locators import LocatorsVacanvies
from config import EXTRA_LONG_PAUSE
from data_tests import auth as td


class VacanciesPage():
    """Sign in page with login method for any type of person"""
    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsVacanvies

    def is_confirmation_sent(self):
        self.browser.pause(EXTRA_LONG_PAUSE)
        text = self.browser.get_text_of_element(self.locators.POP_UP_WINDOW_SIGN_UP_TEXT)
        return text == td.IS_CONFIRMATION_SENT

    def click_confirmation_link(self, link):
        self.browser.driver.get(link)

    def is_instructions_sent(self):
        self.browser.pause(EXTRA_LONG_PAUSE)
        text = self.browser.get_text_of_element(self.locators.POP_UP_WINDOW_FORGOT_PASSWORD_TEXT)
        return text == td.IS_INSTRUCTION_SENT

    def click_ok(self):
        self.browser.click_element(self.locators.POP_UP_WINDOW_FORGOT_PASSWORD_BUTTON)
