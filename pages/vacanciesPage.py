from methods import Methods
from locators import LocatorsVacancies


class VacanciesPage(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsVacancies

    def view_details(self):
        self.click_element(self.locators.DETAILS)

    # def check_pagination_next(self):
    #     self.driver.find_element_by_css_selector(self.pagination_next).click()

    # def check_pagination_previous(self):
    #     self.driver.find_element_by_css_selector(self.pagination_previous).click()

    def check_pagination_next(self):
        self.click_element_by_text(self.locators.PAGINATION_NEXT, 'Next »')

    def check_pagination_previous(self):
        self.click_element_by_text(self.locators.PAGINATION_PREVIOUS, '« Previous')

    def details_text(self):
        tmp = self.pop_up_element(self.locators.VACANCY_INFO).text
        return tmp

    def next_test(self):
        tmp2 = self.pop_up_element(self.locators.NEXT_TEST).text
        return tmp2

    def previous_test(self):
        tmp3 = self.pop_up_element(self.locators.PREVIOUS_TEST).text
        return tmp3
