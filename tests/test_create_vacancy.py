from init import BasePage
from pages.sign_in_page import SignInPage
from pages.create_vacancy_page import CreateVacancyPage
from pages.my_companies_page import MyCompaniesPage
from test_data import CownerData
import time


class TestCreateVacancy(BasePage):

    def test_create_vacancy(self, option='Log in', person='COWNER'):
        sign_in = SignInPage(self)
        create_vacancy = CreateVacancyPage(self)
        my_companies = MyCompaniesPage(self)

        self.header.select_option(option)
        sign_in.login(person)

        self.header.click_my_companies()
        my_companies.click_view_details()
        create_vacancy.click_create_vacancy()
        create_vacancy.enter_vacancy_data(CownerData.VACANCY_DATA)
        create_vacancy.choose_employment()
        create_vacancy.choose_currency()
        create_vacancy.click_add_requirement()
        create_vacancy.enter_requirements(CownerData.REQUIREMENTS)
        create_vacancy.click_vacancy_create()
