from init import SeleniumTestBase


class TestSendResume(SeleniumTestBase):

    def setUp(self):
        self.header.select_option("Log in")
        self.sign_in_page.login("USER")

    def test_send_resume(self):
        self.header.go_to_allVacancies()

        self.vacancies_page.click_viewDetails_button()

        self.view_vacancy_page.click_sendResume_button()

        self.preview_resume_page.click_sendEmail_button()
        msg = self.preview_resume_page.confirmation_message()

        assert msg == "Mail has been sent!"
