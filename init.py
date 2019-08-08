from methods import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT, WEBDRIVER
from pages.companies_page import CompaniesPage
from pages.company_details_page import CompanyDetailsPage
from pages.header import Header
from pages.user_profile_page import UserPage
from pages.sign_in_page import SignInPage
from utilities.db import prepare_db
from unittest import TestCase


class SeleniumTestBase(TestCase):
    """The parent class for all tests"""
    @classmethod
    def setUpClass(cls):
        prepare_db()
        driver = WebdriverSelection().get_webdriver(WEBDRIVER)
        driver.maximize_window()
        driver.get(URL)
        cls.browser = DriverWrapper(driver, TIMEOUT)
        cls.header = Header(cls.browser)
        cls.sign_in_page = SignInPage(cls.browser)
        cls.user_profile_page = UserPage(cls.browser)
        cls.companies_page = CompaniesPage(cls.browser)
        cls.company_details_page = CompanyDetailsPage(cls.browser)

    @classmethod
    def tearDownClass(cls):
        cls.browser.driver.quit()
