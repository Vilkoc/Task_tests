from init import BasePage
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.viewVacancy_page import ViewVacancyPage
from pages.previewResume_page import PreviewResumePage
from pages.editResume_page import EditResumePage
from pages.header import Header
import unittest


ALL_VACANCIES_LINK_TEXT = 'RabotyNet'
VIEW_DETAILS_BUTTON_CSS_SELECTOR = 'a[href="/viewVacancy/6"]'
BUTTONS_CSS_SELECTOR = 'button[class="btn btn-success"]'
MESSAGE_CSS_SELECTOR = 'div[class="wrap"]>p'
SEND_RESUME_BUTTON_CSS_SELECTOR = 'a[class="btn btn-success"]'
POSITION_FIELD_ID = 'position'
PREVIEW_PDF_BUTTON_CSS_SELECTOR = 'button[class="btn btn-success"]'
GET_TEXT_FROM_FIELD = 'ng-reflect-model'
SHOW_ALL_INFO_BUTTON_CSS_SELECTOR = 'a[href="/update/2"]'


class TestChangeData(BasePage):

    def test_change_data(self, option='Log in', person='USER'):
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
        preview_resume_page.click_change_button()

        edit_resume_page = EditResumePage(driver)

        # edit_resume_page.change_positionField('Junior Developer')

        # text = edit_resume_page.confirmation_changes()
        # self.assertEqual(text, 'Junior Developer')



