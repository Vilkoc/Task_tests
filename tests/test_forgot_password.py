import pytest
import allure
from init import resource_setup
from config import EMAIL_SUBJECT_PASSW_RECOVERY, USERNAME_PASSW_RECOVERY, \
    EMAIL_FORGOT_PASSWORD, FROM_FORGOT_PASSWORD, OLD_PASSWORD, NEW_PASSWORD
from utilities.func import login
from utilities.db import change_varification_link


def test_forgot_password(resource_setup):
    """ Testcase to renew password using email"""
    page = resource_setup
    page.header.click_icon()
    page.header.click_log_in()

    page.sign_in_page.click_forgot_password()

    page.forgot_password.enter_login_email(USERNAME_PASSW_RECOVERY)
    page.forgot_password.click_submit_button()

    with allure.step('Is instruction sent on email?'):
        assert page.vacancies.is_instructions_sent()
    page.vacancies.click_ok()

    change_varification_link(USERNAME_PASSW_RECOVERY)
    link = 'http://localhost:4200/confirmPassword?token=3e83667c-c59c-4fda-aa7a-a47346a3cd6a'

    page.vacancies.click_confirmation_link(link)

    page.confirmation_password.enter_new_password(NEW_PASSWORD)
    page.confirmation_password.enter_confirm_password(NEW_PASSWORD)
    page.confirmation_password.click_register_button()

    with allure.step('Pop up window messaging "password restore"'):
        assert page.sign_in_page.is_password_restored()
    page.sign_in_page.click_ok()

    login(page.sign_in_page, USERNAME_PASSW_RECOVERY, OLD_PASSWORD)
    with allure.step('Is user authenticated?'):
        assert page.header.is_logined()
