from init import BasePage
from pages.sign_in_page import SignInPage
from pages.my_companies_page import MyCompaniesPage
from test_data import CownerData
import time


class TestDeleteCompany(BasePage):

    def test_create_vacancy(self, option='Log in', person='COWNER'):
        sign_in = SignInPage(self)
        delete_company = MyCompaniesPage(self)

        self.header.select_option(option)
        sign_in.login(person)

        self.header.click_my_companies()
        delete_company.click_company_delete(CownerData.COMPANY_DELETE)

        check = delete_company.check_company_present(CownerData.COMPANY_DELETE)
        assert check
