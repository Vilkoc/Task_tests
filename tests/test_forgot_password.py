from init import BasePage
import unittest
from pages.header import Header
from pages.auth_page import AuthPage
from pages.vacancies_page import VacanciesPage
from config import EMAIL_SUBJECT_PASSW_RECOVERY, USERNAME_PASSW_RECOVERY, OLD_PASSWORD, NEW_PASSWORD
from utilities.get_email import get_link
from pages.forgot_password_page import ForgotPasswordPage
from pages.confirm_password_page import ConfirmPassword


class TestForgotPassword(BasePage):

    def test_forgot_password(self):
        header = Header(self.driver)
        login = AuthPage(self.driver)
        vacancies = VacanciesPage(self.driver)
        forgot_password = ForgotPasswordPage(self.driver)
        confirmation_password = ConfirmPassword(self.driver)

        header.click_icon()
        header.click_log_in()

        login.click_forgot_password()

        forgot_password.enter_login_email(USERNAME_PASSW_RECOVERY)
        forgot_password.click_submit_button()

        assert vacancies.is_instructions_sent()
        vacancies.click_ok()

        link = get_link(EMAIL_SUBJECT_PASSW_RECOVERY)
        vacancies.click_confirmation_link(link)

        confirmation_password.enter_new_password(NEW_PASSWORD)
        confirmation_password.enter_confirm_password(NEW_PASSWORD)
        confirmation_password.click_register_button()

        assert login.is_password_restored()
        login.click_ok()

        login.login_user(USERNAME_PASSW_RECOVERY, OLD_PASSWORD)
        assert header.is_logined()
