from config import EXTRA_LONG_PAUSE
from locators import LocatorsVacancies
from data_tests import guest_data


class VacanciesPage:
    """On this page user or cowner can view vacancies"""

    def __init__(self, base_obj):
        self.browser = base_obj
        self.locators = LocatorsVacancies

    def is_confirmation_sent(self):
        text = self.browser.get_text_of_element(self.locators.POP_UP_WINDOW_SIGN_UP_TEXT)
        return text == 'User has been created successfully. Confirm your email and login into site!'

    def click_confirmation_link(self, link):
        self.browser.driver.get(link)

    def is_instructions_sent(self):
        self.browser.pause(EXTRA_LONG_PAUSE)
        text = self.browser.get_text_of_element(self.locators.POP_UP_WINDOW_FORGOT_PASSWORD_TEXT)
        return text == 'Please check mail for further instructions!'

    def click_ok(self):
        self.browser.click_element(self.locators.POP_UP_WINDOW_FORGOT_PASSWORD_BUTTON)

    def click_viewDetails_button(self):
        self.browser.click_element(self.locators.VIEW_DETAILS_BUTTON)

    def view_details(self):
        self.browser.click_element(self.locators.DETAILS)

    def check_pagination_next(self):
        self.browser.click_element_by_text(self.locators.PAGINATION_NEXT, guest_data.NEXT)

    def check_pagination_previous(self):
        self.browser.click_element_by_text(self.locators.PAGINATION_PREVIOUS, guest_data.PREVIOUS)

    def details_text(self):
        tmp = self.browser.pop_up_element(self.locators.VACANCY_INFO).text
        return tmp

    def next_test(self):
        tmp2 = self.browser.pop_up_element(self.locators.NEXT_TEST).text
        return tmp2

    def previous_test(self):
        tmp3 = self.browser.pop_up_element(self.locators.PREVIOUS_TEST).text
        return tmp3
