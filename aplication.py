from methods import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.confirm_password_page import ConfirmPassword
from utilities.db import prepare_db
import pytest


class Empty():
    pass


@pytest.fixture()
def resource_setup(request):
    print('start fix')
    prepare_db()
    driver = WebdriverSelection().get_webdriver("Chrome")
    driver.maximize_window()
    driver.get(URL)
    browser = DriverWrapper(driver, TIMEOUT)
    page = Empty()
    page.header = Header(browser)
    page.sign_in_page = SignInPage(browser)
    page.forgot_password = ForgotPasswordPage(browser)
    page.confirmation_password = ConfirmPassword(browser)
    page.vacancies = VacanciesPage(browser)
    def resource_teardown():
        print('finish fix')
        driver.quit()
    request.addfinalizer(resource_teardown)
    return page