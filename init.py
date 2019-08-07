from methods import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT, WEBDRIVER
from pages.header import Header
from pages.user_profile_page import UserPage
from pages.sign_in_page import SignInPage
from utilities.db import prepare_db
from unittest import TestCase
from pages.my_companies_page import MyCompaniesPage
from pages.create_company_page import CreateCompanyPage
from pages.create_vacancy_page import CreateVacancyPage
from pages.view_company_page import ViewCompanyPage
from pages.update_company_page import UpdateCompanyPage


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
        cls.my_companies_page = MyCompaniesPage(cls.browser)
        cls.create_company_page = CreateCompanyPage(cls.browser)
        cls.create_vacancy_page = CreateVacancyPage(cls.browser)
        cls.view_company_page = ViewCompanyPage(cls.browser)
        cls.update_company_page = UpdateCompanyPage(cls.browser)

    @classmethod
    def tearDownClass(cls):
        cls.browser.driver.quit()
