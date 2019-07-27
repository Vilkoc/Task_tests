from init import BasePage
from pages.login_page import LoginPage
from pages.vacancies_page import VacanciesPage
from pages.viewVacancy_page import ViewVacancyPage
from pages.previewResume_page import PreviewResumePage
from pages.editResume_page import EditResumePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import unittest
import time

ALL_VACANCIES_LINK_TEXT = 'RabotyNet'
VIEW_DETAILS_BUTTON_CSS_SELECTOR = 'a[href="/viewVacancy/10"]'
BUTTONS_CSS_SELECTOR = 'button[class="btn btn-success"]'
MESSAGE_CSS_SELECTOR = 'div[class="wrap"]>p'
SEND_RESUME_BUTTON_CSS_SELECTOR = 'a[class="btn btn-success"]'
POSITION_FIELD_ID = 'position'
PREVIEW_PDF_BUTTON_CSS_SELECTOR = 'button[class="btn btn-success"]'
GET_TEXT_FROM_FIELD = 'ng-reflect-model'


class TestChangeData(BasePage):

    def test_change_data(self):
        driver = self.driver

        login_page = LoginPage(driver)
        login_page.login('user@gmail.com', 'user')

        vacancies_page = VacanciesPage(driver)
        time.sleep(3)
        vacancies_page.go_to_allVacancies()
        self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, VIEW_DETAILS_BUTTON_CSS_SELECTOR)))
        vacancies_page.click_viewDetails_button()

        view_vacancy_page = ViewVacancyPage(driver)
        self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, SEND_RESUME_BUTTON_CSS_SELECTOR)))
        view_vacancy_page.click_sendResume_button()

        preview_resume_page = PreviewResumePage(driver)
        self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, BUTTONS_CSS_SELECTOR)))
        preview_resume_page.click_change_button()

        edit_resume_page = EditResumePage(driver)
        self.wait.until(ec.element_to_be_clickable((By.ID, POSITION_FIELD_ID)))

        edit_resume_page.change_positionField('Middle Developer')
        edit_resume_page.click_previewPDF_button()
        time.sleep(5)
        self.wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, PREVIEW_PDF_BUTTON_CSS_SELECTOR)))
        preview_resume_page.click_change_button()

        text = edit_resume_page.confirmation_changes()
        self.assertEqual(text, 'Middle Developer')


if __name__ == '__main__':
    unittest.main()
