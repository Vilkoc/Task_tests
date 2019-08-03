from init import BasePage
from pages.hotVacanciesPage import HotVacanciesPage


class VacanciesTest(BasePage):

    def test_hot_vacancies(self):
        driver = self.driver

        details = HotVacanciesPage(driver)
        details.view_details()
        driver.back()

        vacancy_info = HotVacanciesPage(driver)
        text = vacancy_info.details_text()
        self.assertEqual(text, "Junior Engineer")

        # driver.execute_script('window.scrollTo(200,200)')
        pagination_next = HotVacanciesPage(driver)
        pagination_next.check_pagination_next()

        nextbutton = HotVacanciesPage(driver)
        tet = nextbutton.next_test()
        self.assertEqual(tet, "Junior Engineer")

        pagination_previous = HotVacanciesPage(driver)
        pagination_previous.check_pagination_previous()

        previusbutton = HotVacanciesPage(driver)
        tot = previusbutton.previous_test()
        self.assertEqual(tot, "Junior Engineer")
