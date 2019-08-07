from init import BasePage
from pages.sign_in_page import SignInPage
from pages.update_company_page import UpdateCompanyPage
from pages.my_companies_page import MyCompaniesPage
from data_tests.cowner_data import CownerData


class TestUpdateCompanyName(BasePage):

    def __init__(self):
        self.sign_in = SignInPage(self)
        self.update_company = UpdateCompanyPage(self)
        self.my_companies = MyCompaniesPage(self)

    def test_update_company_name(self):
        self.header.select_option(CownerData.OPTION)
        self.sign_in.login(CownerData.PERSON)

        self.header.click_my_companies()
        self.my_companies.click_update(CownerData.COMPANY_FOR_UDATING)
        self.update_company.update_company_name(CownerData.COMPANY_RENAME)
        self.update_company.click_update_company_button()
        self.my_companies.click_update(CownerData.COMPANY_RENAME)
        a = self.update_company.check_company_name()
        assert a == CownerData.COMPANY_RENAME




