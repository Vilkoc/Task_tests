from init import SeleniumTestBase
import unittest
from pages.auth_page import AuthPage
from pages.vacancies_page import VacanciesPage
from config import EMAIL_SUBJECT_PASSW_RECOVERY, USERNAME_PASSW_RECOVERY, \
    EMAIL_FORGOT_PASSWORD, FROM_FORGOT_PASSWORD, OLD_PASSWORD, NEW_PASSWORD
from utilities.get_email import get_link
from utilities.func import login
from pages.forgot_password_page import ForgotPasswordPage
from pages.confirm_password_page import ConfirmPassword


class TestForgotPassword(SeleniumTestBase):
    # @unittest.skip('skip, as password doesnt change')
    def test_forgot_password(self):

        self.header.click_icon()
        self.header.click_log_in()

        self.sign_in_page.click_forgot_password()

        self.forgot_password.enter_login_email(USERNAME_PASSW_RECOVERY)
        self.forgot_password.click_submit_button()

        assert self.vacancies.is_instructions_sent()
        self.vacancies.click_ok()

        link = get_link(EMAIL_FORGOT_PASSWORD, FROM_FORGOT_PASSWORD, EMAIL_SUBJECT_PASSW_RECOVERY)
        self.vacancies.click_confirmation_link(link)

        self.confirmation_password.enter_new_password(NEW_PASSWORD)
        self.confirmation_password.enter_confirm_password(NEW_PASSWORD)
        self.confirmation_password.click_register_button()

        assert self.sign_in_page.is_password_restored()
        self.sign_in_page.click_ok()

        login(USERNAME_PASSW_RECOVERY, OLD_PASSWORD)
        assert self.header.is_logined()
