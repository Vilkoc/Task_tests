from methods import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT, WEBDRIVER
from utilities.db import prepare_db
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.view_vacancy_page import ViewVacancyPage
from pages.preview_resume_page import PreviewResumePage
from pages.edit_resume_page import EditResumePage
import pytest


@pytest.fixture(scope='function')
def setup():
    driver = WebdriverSelection().get_webdriver(WEBDRIVER)
    driver.maximize_window()
    driver.get(URL)
    browser = DriverWrapper(driver, TIMEOUT)
    page_dict = {'header': Header(browser), 'sign_in_page': SignInPage(browser), 'vacancies_page': VacanciesPage(browser),
                 'view_vacancy_page': ViewVacancyPage(browser), 'preview_resume_page': PreviewResumePage(browser),
                 'edit_resume_page': EditResumePage(browser)}
    yield page_dict
    browser.driver.quit()


# @pytest.fixture(scope='function')
# def page_init(setup):
#     page_dict = {'header': Header(setup), 'sign_in_page': SignInPage(setup), 'vacancies_page': VacanciesPage(setup),
#                  'view_vacancy_page': ViewVacancyPage(setup), 'preview_resume_page': PreviewResumePage(setup),
#                  'edit_resume_page': EditResumePage(setup)}
#     return page_dict


@pytest.fixture(scope='session')
def clean_db():
    prepare_db()
