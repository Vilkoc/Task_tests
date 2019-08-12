from init import BasePage
from pages.sign_in_page import SignInPage
from pages.create_company_page import CreateCompanyPage
from pages.my_companies_page import MyCompaniesPage
from data_tests.cowner_data import CownerData


class TestCreateCompany(BasePage):

    def test_create_company(self):
        sign_in = SignInPage(self)
        create_company = CreateCompanyPage(self)
        my_companies = MyCompaniesPage(self)

        self.header.select_option(CownerData.OPTION)
        sign_in.login(CownerData.PERSON)

        self.header.click_create_company()
        create_company.enter_data(CownerData.COMPANY_DATA)
        create_company.click_create_button()
        self.header.click_my_companies()
        my_companies.click_update(CownerData.COMPANY_CREATE)
        z = create_company.read_data()

        j = 0
        for i in CownerData.COMPANY_DATA:
            assert i == z[j]
            j += 1
