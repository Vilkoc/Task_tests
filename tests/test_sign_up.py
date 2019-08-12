from data_tests.auth import EMAIL_SUBJECT_SIGNUP, USERNAME_SIGNUP, PASSWORD, EMAIL_SIGNUP, FROM_SIGNUP
import pytest
import allure
from init import resource_setup
from utilities.func import login
from utilities.db import change_varification_link, wait_user_update

def test_sign_up(resource_setup):
    """ Testcase for sign up user. """
    page = resource_setup
    page.header.click_icon()
    page.header.click_log_in()

    page.sign_in_page.click_sign_up_tab()

    page.sign_in_page.enter_sign_up_email(USERNAME_SIGNUP)
    page.sign_in_page.enter_sign_up_password(PASSWORD)
    page.sign_in_page.enter_sign_up_matching_password(PASSWORD)
    page.sign_in_page.click_sing_up_button()

    with allure.step('Is confirmation sent on email?'):
        assert page.vacancies.is_confirmation_sent()

    change_varification_link(USERNAME_SIGNUP)
    link = 'http://localhost:4200/users/auth/confirm?token=3e83667c-c59c-4fda-aa7a-a47346a3cd6a'
    page.vacancies.click_confirmation_link(link)

    wait_user_update(USERNAME_SIGNUP)

    login(page.sign_in_page, USERNAME_SIGNUP, PASSWORD)
    with allure.step('Is user authenticated?'):
        assert page.header.is_logined()


def test_sign_up_negative_email(resource_setup):
    """ Testcase for sign up user.
    Negative. Using email already registered user"""
    page = resource_setup
    page.header.click_icon()
    page.header.click_log_in()

    page.sign_in_page.click_sign_up_tab()

    page.sign_in_page.enter_sign_up_email("user@gmail.com")
    page.sign_in_page.enter_sign_up_password(PASSWORD)
    page.sign_in_page.enter_sign_up_matching_password(PASSWORD)
    page.sign_in_page.click_sing_up_button()

    with allure.step('Is email already taken?'):
        assert page.vacancies.is_email_taken()


def test_sign_up_negative_password(resource_setup):
    """ Testcase for sign up user.
    Negative. Using incorect password """
    page = resource_setup
    page.header.click_icon()
    page.header.click_log_in()

    page.sign_in_page.click_sign_up_tab()

    page.sign_in_page.enter_sign_up_email("user@gmail.com")
    page.sign_in_page.enter_sign_up_password("yneoi")
    page.sign_in_page.enter_sign_up_matching_password("yneoi")
    page.sign_in_page.click_sing_up_button()

    with allure.step('Is message about wrong password?'):
        assert page.sign_in_page.is_password_sign_up_wrong()

def test_sign_up_negative_email_wrong(resource_setup):
    """ Testcase for sign up user.
    Negative. Using incorect email """
    page = resource_setup
    page.header.click_icon()
    page.header.click_log_in()

    page.sign_in_page.click_sign_up_tab()

    page.sign_in_page.enter_sign_up_email("user@gmail")
    page.sign_in_page.enter_sign_up_password(PASSWORD)
    page.sign_in_page.enter_sign_up_matching_password(PASSWORD)
    page.sign_in_page.click_sing_up_button()

    with allure.step('Is message about wrong email?'):
        assert page.sign_in_page.is_email_wrong()

def test_sign_up_negative_password_mismatch(resource_setup):
    """ Testcase for sign up user.
    Negative. Using differen password and matching password """
    page = resource_setup
    page.header.click_icon()
    page.header.click_log_in()

    page.sign_in_page.click_sign_up_tab()

    page.sign_in_page.enter_sign_up_email("user@gmail.com")
    page.sign_in_page.enter_sign_up_password(PASSWORD)
    page.sign_in_page.enter_sign_up_matching_password(PASSWORD+'a')
    page.sign_in_page.click_sing_up_button()

    with allure.step('Is message about different passwords?'):
        assert page.sign_in_page.is_psswords_mismatch()

