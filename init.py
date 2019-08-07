from methods import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT, WEBDRIVER
from pages.header import Header
from pages.user_profile_page import UserPage
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.view_vacancy_page import ViewVacancyPage
from pages.preview_resume_page import PreviewResumePage
from pages.edit_resume_page import EditResumePage
from pages.view_company_page import ViewCompanyPage
from pages.companies_page import CompaniesPage
from utilities.db import prepare_db
from unittest import TestCase


class SeleniumTestBase(TestCase):
    """The parent class for all tests"""

    @classmethod
    def setUpClass(cls):
        # prepare_db()
        driver = WebdriverSelection().get_webdriver(WEBDRIVER)
        driver.maximize_window()
        driver.get(URL)
        cls.browser = DriverWrapper(driver, TIMEOUT)
        cls.header = Header(cls.browser)
        cls.sign_in_page = SignInPage(cls.browser)
        cls.user_profile_page = UserPage(cls.browser)
        cls.vacancies_page = VacanciesPage(cls.browser)
        cls.view_vacancy_page = ViewVacancyPage(cls.browser)
        cls.preview_resume_page = PreviewResumePage(cls.browser)
        cls.edit_resume_page = EditResumePage(cls.browser)
        cls.view_company_page = ViewCompanyPage(cls.browser)
        cls.companies_page = CompaniesPage(cls.browser)

    @classmethod
    def tearDownClass(cls):
        cls.browser.driver.quit()
