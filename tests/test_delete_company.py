from init import BasePage
from pages.sign_in_page import SignInPage
from pages.my_companies_page import MyCompaniesPage
from data_tests.cowner_data import CownerData
import unittest


class TestDeleteCompany(BasePage):

    @unittest.skip('skip, as password doesnt change')
    def test_create_vacancy(self):
        sign_in = SignInPage(self)
        delete_company = MyCompaniesPage(self)

        self.header.select_option(CownerData.OPTION)
        sign_in.login(CownerData.PERSON)

        self.header.click_my_companies()
        delete_company.click_company_delete(CownerData.COMPANY_DELETE)

        check = delete_company.check_company_present(CownerData.COMPANY_DELETE)
        assert check
