from init import BasePage
from pages.sign_in_page import SignInPage
from pages.update_company_page import UpdateCompanyPage
from pages.my_companies_page import MyCompaniesPage
from test_data import CownerData


class TestUpdateCompanyName(BasePage):

    def test_update_company_name(self, option='Log in',  person='COWNER'):
        sign_in = SignInPage(self)
        update_company = UpdateCompanyPage(self)
        my_companies = MyCompaniesPage(self)

        self.header.select_option(option)
        sign_in.login(person)

        self.header.click_my_companies()
        my_companies.click_company_update()
        update_company.update_company_name(CownerData.COMPANY_RENAME)
        a = update_company.check_company_name()
        assert a == CownerData.COMPANY_RENAME
        update_company.click_update_company_button()





