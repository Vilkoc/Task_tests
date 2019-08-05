from init import BasePage
from pages.vacancies_page import VacanciesPage
from data_tests import guest_data


class TestVacancies(BasePage):

    def test_vacancies(self):

        details = VacanciesPage(self)
        details.view_details()
        self.browser.driver.back()

        text1 = details.details_text()
        assert text1 == guest_data.TOP_VACANCY

        details.check_pagination_next()

        text2 = details.next_test()
        assert text2 == guest_data.TOP_VACANCY

        details.check_pagination_previous()

        text3 = details.previous_test()
        assert text3 == guest_data.TOP_VACANCY
