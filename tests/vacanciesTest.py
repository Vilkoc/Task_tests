from init import BasePage
from pages.vacanciesPage import VacanciesPage


class VacanciesTest(BasePage):

    def test_vacancies(self):
        driver = self.driver

        details = VacanciesPage(driver)
        details.view_details()
        driver.back()

        vacancy_info = VacanciesPage(driver)
        text = vacancy_info.details_text()
        self.assertEqual(text, "Junior Engineer")

        pagination_next = VacanciesPage(driver)
        pagination_next.check_pagination_next()

        nextbutton = VacanciesPage(driver)
        tet = nextbutton.next_test()
        self.assertEqual(tet, "Junior Engineer")

        pagination_previous = VacanciesPage(driver)
        pagination_previous.check_pagination_previous()

        previusbutton = VacanciesPage(driver)
        tot = previusbutton.previous_test()
        self.assertEqual(tot, "Junior Engineer")
