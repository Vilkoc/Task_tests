from init import BasePage
from pages.vacanciesPage import VacanciesPage


class VacanciesTest(BasePage):

    def test_vacancies(self):

        details = VacanciesPage(self)
        details.view_details()
        self.browser.driver.back()

        text1 = details.details_text()
        assert text1 == "Junior Engineer"

        details.check_pagination_next()

        text2 = details.next_test()
        assert text2 == "Junior Engineer"

        details.check_pagination_previous()

        text3 = details.previous_test()
        assert text3 == "Junior Engineer"
