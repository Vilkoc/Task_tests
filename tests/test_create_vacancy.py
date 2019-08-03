from init import BasePage
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.create_vacancy_page import CreateVacancyPage
from pages.my_companies_page import MyCompaniesPage
from test_data import CownerData
import time


class TestCreateVacancy(BasePage):

    def test_create_vacancy(self, option='Log in', person='COWNER'):
        driver = self.driver
        sign_in = SignInPage(driver)
        header = Header(driver)
        create_vacancy = CreateVacancyPage(driver)
        my_companies = MyCompaniesPage(driver)

        header.select_option(option)
        sign_in.login(person)

        my_companies.click_my_companies()
        my_companies.click_view_details()
        create_vacancy.click_create_vacancy()
        create_vacancy.enter_vacancy_data(CownerData.VACANCY_DATA)
        create_vacancy.choose_employment()
        time.sleep(1)
        create_vacancy.choose_currency()
        time.sleep(1)
        create_vacancy.click_add_requirement()
        time.sleep(3)
        create_vacancy.enter_requirements(CownerData.REQUIREMENTS)
        time.sleep(3)
        create_vacancy.click_vacancy_create()
