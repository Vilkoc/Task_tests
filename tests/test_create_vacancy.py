from init import BasePage
from pages.sign_in_page import SignInPage
from pages.create_vacancy_page import CreateVacancyPage
from pages.my_companies_page import MyCompaniesPage
from pages.view_company_page import ViewCompanyPage
from data_tests.cowner_data import CownerData


class TestCreateVacancy(BasePage):

    @unittest.skip('skip, as password doesnt change')
    def test_create_vacancy(self):
        sign_in = SignInPage(self)
        create_vacancy = CreateVacancyPage(self)
        my_companies = MyCompaniesPage(self)
        view_company = ViewCompanyPage(self)

        self.header.select_option(CownerData.OPTION)
        sign_in.login(CownerData.PERSON)

        self.header.click_my_companies()
        my_companies.click_view_details()
        view_company.click_create_vacancy()
        create_vacancy.enter_vacancy_data(CownerData.VACANCY_DATA)
        create_vacancy.choose_employment()
        create_vacancy.choose_currency()
        create_vacancy.click_add_requirement()
        create_vacancy.enter_requirements(CownerData.REQUIREMENTS)
        create_vacancy.click_vacancy_create()
        view_company.view_vacancy_details(CownerData.VACANCY_NAME)
        z = create_vacancy.read_vacancy_data()

        j = 0
        for i in CownerData.VACANCY_DATA:
            assert i == z[j]
            j += 1
