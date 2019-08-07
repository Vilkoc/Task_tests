from init import SeleniumTestBase


class TestChangeData(SeleniumTestBase):

    def setUp(self):
        self.header.select_option("Log in")
        self.sign_in_page.login("USER")

    def test_change_data(self):
        self.header.go_to_allVacancies()

        self.vacancies_page.click_viewDetails_button()

        self.view_vacancy_page.click_sendResume_button()

        self.preview_resume_page.click_change_button()

        self.edit_resume_page.change_positionField("Middle Developer")
        self.edit_resume_page.click_previewPDF_button()

        self.preview_resume_page.click_change_button()

        text = self.edit_resume_page.confirmation_changes()
        assert text == "Middle Developer"
