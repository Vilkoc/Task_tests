from data_tests.auth import USERNAME_PASSW_RECOVERY
from init import BasePage
import unittest
from pages.auth_page import AuthPage
from pages.vacancies_page import VacanciesPage
from data_tests import auth as td
from utilities.get_email import get_link
from pages.forgot_password_page import ForgotPasswordPage
from pages.confirm_password_page import ConfirmPassword


class TestForgotPassword(BasePage):
    @unittest.skip('skip, as password doesnt change')
    def test_forgot_password(self):
        login = AuthPage(self)
        vacancies = VacanciesPage(self)
        forgot_password = ForgotPasswordPage(self)
        confirmation_password = ConfirmPassword(self)

        self.header.click_icon()
        self.header.click_log_in()

        login.click_forgot_password()

        forgot_password.enter_login_email(td.USERNAME_PASSW_RECOVERY)
        forgot_password.click_submit_button()

        assert vacancies.is_instructions_sent()
        vacancies.click_ok()

        link = get_link(td.EMAIL_FORGOT_PASSWORD, td.FROM_FORGOT_PASSWORD, td.EMAIL_SUBJECT_PASSW_RECOVERY)
        vacancies.click_confirmation_link(link)

        confirmation_password.enter_new_password(td.NEW_PASSWORD)
        confirmation_password.enter_confirm_password(td.NEW_PASSWORD)
        confirmation_password.click_register_button()

        assert login.is_password_restored()
        login.click_ok()

        login.login_user(td.USERNAME_PASSW_RECOVERY, td.OLD_PASSWORD)
        assert self.header.is_logined()
