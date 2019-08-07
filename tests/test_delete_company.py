from init import BasePage
from pages.sign_in_page import SignInPage
from pages.my_companies_page import MyCompaniesPage
from data_tests.cowner_data import CownerData


class TestDeleteCompany(BasePage):

    def __init__(self):
        self.sign_in = SignInPage(self)
        self.delete_company = MyCompaniesPage(self)

    def test_create_vacancy(self):
        self.header.select_option(CownerData.OPTION)
        self.sign_in.login(CownerData.PERSON)

        self.header.click_my_companies()
        self.delete_company.click_company_delete(CownerData.COMPANY_DELETE)

        check = self.delete_company.check_company_present(CownerData.COMPANY_DELETE)
        assert check
