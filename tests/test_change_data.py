from init import BasePage
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.viewVacancy_page import ViewVacancyPage
from pages.previewResume_page import PreviewResumePage
from pages.editResume_page import EditResumePage


class TestChangeData(BasePage):

    def test_change_data(self, option='Log in', person='USER'):
        sign_in_page = SignInPage(self)

        self.header.select_option(option)
        sign_in_page.login(person)

        self.header.go_to_allVacancies()

        vacancies_page = VacanciesPage(self)
        vacancies_page.click_viewDetails_button()

        view_vacancy_page = ViewVacancyPage(self)
        view_vacancy_page.click_sendResume_button()

        preview_resume_page = PreviewResumePage(self)
        preview_resume_page.click_change_button()

        edit_resume_page = EditResumePage(self)
        edit_resume_page.change_positionField('Middle Developer')
        edit_resume_page.click_previewPDF_button()

        preview_resume_page.click_change_button()

        text = edit_resume_page.confirmation_changes()
        assert text == 'Middle Developer'
