from init import BasePage
from pages.sign_in_page import SignInPage
from pages.create_vacancy_page import CreateVacancyPage
from pages.my_companies_page import MyCompaniesPage
from pages.view_company_page import ViewCompanyPage
from data_tests.cowner_data import CownerData


class TestCreateVacancy(BasePage):

    def __init__(self):
        self.sign_in = SignInPage(self)
        self.create_vacancy = CreateVacancyPage(self)
        self.my_companies = MyCompaniesPage(self)
        self.view_company = ViewCompanyPage(self)

    def test_create_vacancy(self):
        self.header.select_option(CownerData.OPTION)
        self.sign_in.login(CownerData.PERSON)

        self.header.click_my_companies()
        self.my_companies.click_view_details()
        self.view_company.click_create_vacancy()
        self.create_vacancy.enter_vacancy_data(CownerData.VACANCY_DATA)
        self.create_vacancy.choose_employment()
        self.create_vacancy.choose_currency()
        self.create_vacancy.click_add_requirement()
        self.create_vacancy.enter_requirements(CownerData.REQUIREMENTS)
        self.create_vacancy.click_vacancy_create()
        self.view_company.view_vacancy_details(CownerData.VACANCY_NAME)
        z = self.create_vacancy.read_vacancy_data()

        j = 0
        for i in CownerData.VACANCY_DATA:
            assert i == z[j]
            j += 1
