from locators import LocatorsHotVacancies
from data_tests import guest_data


class HotVacanciesPage():
    """On this page users can view details of hot vacancies"""

    def __init__(self, base_obj):
        self.locators = LocatorsHotVacancies
        self.browser = base_obj.browser

    def view_details(self):
        self.browser.click_element(self.locators.HOT_DETAILS)

    def check_pagination_next(self):
        self.browser.click_element(self.locators.HOT_VACANCY_PAGE)
        self.browser.click_element_by_text(self.locators.HOT_PAGINATION_NEXT, guest_data.HOT_NEXT)

    def check_pagination_previous(self):
        self.browser.click_element_by_text(self.locators.HOT_PAGINATION_PREVIOUS, guest_data.HOT_PREVIOUS)

    def details_text(self):
        tmp = self.browser.pop_up_element(self.locators.HOT_VACANCY_INFO).text
        return tmp

    def next_test(self):
        tmp2 = self.browser.pop_up_element(self.locators.HOT_NEXT_TEST).text
        return tmp2

    def previous_test(self):
        tmp3 = self.browser.pop_up_element(self.locators.HOT_PREVIOUS_TEST).text
        return tmp3
