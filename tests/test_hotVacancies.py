from init import SeleniumTestBase
from data_tests import guest_data



class TestVacancies(SeleniumTestBase):

    def test_hot_vacancies(self):

        self.hot_vacancies_page.view_details()
        self.browser.driver.back()

        text1 = self.hot_vacancies_page.details_text()
        assert text1 == guest_data.TOP_VACANCY

        self.hot_vacancies_page.check_pagination_next()

        text2 = self.hot_vacancies_page.next_test()
        assert text2 == guest_data.TOP_VACANCY

        self.hot_vacancies_page.check_pagination_previous()

        text3 = self.hot_vacancies_page.previous_test()
        assert text3 == guest_data.TOP_VACANCY
