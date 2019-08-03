from init import BasePage
from pages.vacanciesPage import VacanciesPage


class VacanciesTest(BasePage):

    def test_vacancies(self):

        details = VacanciesPage(self)
        details.view_details()
        self.browser.driver.back()

        text = details.details_text()
        assert text == "Junior Engineer"

        details.check_pagination_next()

        tet = details.next_test()
        assert tet == "Junior Engineer"

        details.check_pagination_previous()

        tot = details.previous_test()
        assert tot == "Junior Engineer"
