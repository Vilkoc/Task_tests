from init import BasePage
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.viewVacancy_page import ViewVacancyPage
from pages.previewResume_page import PreviewResumePage


class TestSendResume(BasePage):

    def test_send_resume(self, option='Log in', person='USER'):
        sign_in_page = SignInPage(self)

        self.header.select_option(option)
        sign_in_page.login(person)

        self.header.go_to_allVacancies()

        vacancies_page = VacanciesPage(self)
        vacancies_page.click_viewDetails_button()

        view_vacancy_page = ViewVacancyPage(self)
        view_vacancy_page.click_sendResume_button()

        preview_resume_page = PreviewResumePage(self)
        preview_resume_page.click_sendEmail_button()
        msg = preview_resume_page.confirmation_message()

        # self.assertEqual(msg, 'Mail has been sent!')
        assert msg == 'Mail has been sent!'

