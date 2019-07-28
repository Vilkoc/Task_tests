from init import BasePage
from pages.login_page import LoginPage
from pages.vacancies_page import VacanciesPage
from pages.viewVacancy_page import ViewVacancyPage
from pages.previewResume_page import PreviewResumePage
from selenium.webdriver.common.by import By
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


class TestSendResume(BasePage):

    def test_send_resume(self):
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
        preview_resume_page.click_sendEmail_button()

        self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, MESSAGE_CSS_SELECTOR)))
        msg = preview_resume_page.confirmation_message()
        self.assertEqual(msg, 'Mail has been sent!')


if __name__ == '__main__':
    unittest.main()
