from init import BasePage
import unittest
from pages.header import Header
from pages.auth_page import AuthPage
from pages.vacancies_page import VacanciesPage
from config import EMAIL_SUBJECT_SIGNUP, USERNAME_SIGNUP, PASSWORD
from utilities.get_email import get_link


class TestSignUp(BasePage):

    def test_sign_up(self):
        header = Header(self.driver)
        page = AuthPage(self.driver)
        vacancies = VacanciesPage(self.driver)

        header.click_icon()
        header.click_log_in()

        page.click_sign_up_tab()

        page.enter_sign_up_email(USERNAME_SIGNUP)
        page.enter_sign_up_password(PASSWORD)
        page.enter_sign_up_matching_password(PASSWORD)
        page.click_sing_up_button()

        assert vacancies.is_confirmation_sent()

        link = get_link(EMAIL_SUBJECT_SIGNUP)
        vacancies.click_confirmation_link(link)

        page.login_user(USERNAME_SIGNUP, PASSWORD)
        assert header.is_logined()

