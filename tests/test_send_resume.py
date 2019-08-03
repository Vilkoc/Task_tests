from init import BasePage
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.viewVacancy_page import ViewVacancyPage
from pages.previewResume_page import PreviewResumePage
from pages.header import Header


class TestSendResume(BasePage):

    def test_send_resume(self, option='Log in', person='USER'):
        driver = self.driver

        header = Header(driver)
        sign_in_page = SignInPage(driver)

        header.select_option(option)
        sign_in_page.login(person)

        header.go_to_allVacancies()

        vacancies_page = VacanciesPage(driver)
        vacancies_page.click_viewDetails_button()

        view_vacancy_page = ViewVacancyPage(driver)
        view_vacancy_page.click_sendResume_button()

        preview_resume_page = PreviewResumePage(driver)
        preview_resume_page.click_sendEmail_button()
        msg = preview_resume_page.confirmation_message()

        self.assertEqual(msg, 'Mail has been sent!')

