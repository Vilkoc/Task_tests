from init import BasePage
from pages.sign_in_page import SignInPage
from pages.create_company_page import CreateCompanyPage
from pages.my_companies_page import MyCompaniesPage
from data_tests.cowner_data import CownerData


class TestCreateCompany(BasePage):

    def __init__(self):
        self.sign_in = SignInPage(self)
        self.create_company = CreateCompanyPage(self)
        self.my_companies = MyCompaniesPage(self)

    def test_create_company(self):
        self.header.select_option(CownerData.OPTION)
        self.sign_in.login(CownerData.PERSON)
        self.header.click_create_company()
        self.create_company.enter_data(CownerData.COMPANY_DATA)
        self.create_company.click_create_button()
        self.header.click_my_companies()
        self.my_companies.click_update(CownerData.COMPANY_CREATE)
        z = self.create_company.read_data()

        j = 0
        for i in CownerData.COMPANY_DATA:
            assert i == z[j]
            j += 1
