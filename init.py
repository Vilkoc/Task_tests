from methods import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT
from pages.header import Header
from pages.user_profile_page import UserPage
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.confirm_password_page import ConfirmPassword
from utilities.db import prepare_db
from unittest import TestCase
import os


class SeleniumTestBase(TestCase):
    """The parent class for all tests"""
    @classmethod
    def setUpClass(cls):
        prepare_db()
        driver = WebdriverSelection().get_webdriver("Chrome")
        driver.maximize_window()
        driver.get(URL)
        cls.browser = DriverWrapper(driver, TIMEOUT)
        cls.header = Header(cls.browser)
        cls.sign_in_page = SignInPage(cls.browser)
        cls.forgot_password = ForgotPasswordPage(cls.browser)
        cls.confirmation_password = ConfirmPassword(cls.browser)
        cls.user_profile_page = UserPage(cls.browser)
        cls.vacancies = VacanciesPage(cls.browser)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.browser.driver.quit()
