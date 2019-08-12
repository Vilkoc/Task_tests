from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.view_vacancy_page import ViewVacancyPage
from pages.preview_resume_page import PreviewResumePage
import pytest
from init import setup


@pytest.mark.usefixtures('setup')
class TestSendResume():

    def test_send_resume(self):
        self.header = Header(self.browser)
        self.sign_in_page = SignInPage(self.browser)
        self.vacancies_page = VacanciesPage(self.browser)
        self.view_vacancy_page = ViewVacancyPage(self.browser)
        self.preview_resume_page = PreviewResumePage(self.browser)
        self.header.select_option("Log in")
        self.sign_in_page.login("USER")
        self.header.go_to_allVacancies()

        self.vacancies_page.click_viewDetails_button()

        self.view_vacancy_page.click_sendResume_button()

        self.preview_resume_page.click_sendEmail_button()
        msg = self.preview_resume_page.confirmation_message()

        assert msg == "Mail has been sent!"
