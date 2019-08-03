from init import BasePage
from pages.hotVacanciesPage import HotVacanciesPage


class VacanciesTest(BasePage):

    def test_hot_vacancies(self):

        details = HotVacanciesPage(self)
        details.view_details()
        self.browser.driver.back()

        text = details.details_text()
        assert text == "Junior Engineer"

        # driver.execute_script('window.scrollTo(200,200)')
        details.check_pagination_next()

        tet = details.next_test()
        assert tet == "Junior Engineer"

        details.check_pagination_previous()

        tot = details.previous_test()
        assert tot == "Junior Engineer"
