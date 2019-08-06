from init import BasePage
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.view_vacancy_page import ViewVacancyPage
from pages.preview_resume_page import PreviewResumePage
from pages.edit_resume_page import EditResumePage
from data_tests import test_data_Nazar as td


class TestChangeData(BasePage):

    @unittest.skip('skip, as password doesnt change')
    def test_change_data(self):
        sign_in_page = SignInPage(self)

        self.header.select_option(td.LOG_IN)
        sign_in_page.login(td.USER)

        self.header.go_to_allVacancies()

        vacancies_page = VacanciesPage(self)
        vacancies_page.click_viewDetails_button()

        view_vacancy_page = ViewVacancyPage(self)
        view_vacancy_page.click_sendResume_button()

        preview_resume_page = PreviewResumePage(self)
        preview_resume_page.click_change_button()

        edit_resume_page = EditResumePage(self)
        edit_resume_page.change_positionField(td.POSITION_FIELD)
        edit_resume_page.click_previewPDF_button()

        preview_resume_page.click_change_button()

        text = edit_resume_page.confirmation_changes()
        assert text == td.POSITION_FIELD
