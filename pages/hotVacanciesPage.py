from methods import Methods
from locators import LocatorsHotVacancies


class HotVacanciesPage(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsHotVacancies

    def view_details(self):
        self.click_element(self.locators.HOT_DETAILS)

    # def check_pagination_next(self):
    #     self.driver.find_element_by_xpath(self.pagination_next).click()
    #
    # def check_pagination_previous(self):
    #     self.driver.find_element_by_xpath(self.pagination_previous).click()

    def check_pagination_next(self):
        self.click_element_by_text(self.locators.HOT_PAGINATION_NEXT, 'Next»')
        # buttons = self.driver.find_elements_by_css_selector(self.pagination_next)
        # next_page = None
        # for i in buttons:
        #     if i.text == 'Next»':
        #         next_page = i
        # return next_page.click()

    def check_pagination_previous(self):
        self.click_element_by_text(self.locators.HOT_PAGINATION_PREVIOUS, '«Previous')
        # buttons = self.driver.find_elements_by_css_selector(self.pagination_previous)
        # previous_page = None
        # for i in buttons:
        #     if i.text == '«Previous':
        #         previous_page = i
        # return previous_page.click()

    def details_text(self):
        tmp = self.pop_up_element(self.locators.HOT_VACANCY_INFO).text
        return tmp

    def next_test(self):
        tmp2 = self.pop_up_element(self.locators.HOT_NEXT_TEST).text
        return tmp2

    def previous_test(self):
        tmp3 = self.pop_up_element(self.locators.HOT_PREVIOUS_TEST).text
        return tmp3
