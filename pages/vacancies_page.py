from methods import Methods
from locators import LocatorsVacanvies
from credentials import Credentials


class VacanciesPage(Methods):
    """Sign in page with login method for any type of person"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsVacanvies

    def is_confirmation_sent(self):
        window = self.find_pop_up_window()
        text = window.find_element_by_tag_name(self.locators.POP_UP_WINDOW_SIGN_UP_TEXT).text
        print('confirmation:', text)
        return text == self.pop_up_window_sign_up_text

    def click_confirmation_link(self, link):
        self.driver.get(link)
