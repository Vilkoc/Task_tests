from locators import LocatorsVacancies


class VacanciesPage():
    """On this page users can view details"""

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsVacancies

    def view_details(self):
        self.browser.click_element(self.locators.DETAILS)

    def check_pagination_next(self):
        self.browser.click_element_by_text(self.locators.PAGINATION_NEXT, 'Next »')

    def check_pagination_previous(self):
        self.browser.click_element_by_text(self.locators.PAGINATION_PREVIOUS, '« Previous')

    def details_text(self):
        tmp = self.browser.pop_up_element(self.locators.VACANCY_INFO).text
        return tmp

    def next_test(self):
        tmp2 = self.browser.pop_up_element(self.locators.NEXT_TEST).text
        return tmp2

    def previous_test(self):
        tmp3 = self.browser.pop_up_element(self.locators.PREVIOUS_TEST).text
        return tmp3
