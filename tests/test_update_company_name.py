from init import BasePage
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.update_company_page import UpdateCompanyPage
from pages.my_companies_page import MyCompaniesPage
from test_data import CownerData



class TestUpdateCompanyName(BasePage):

    def test_update_company_name(self, option='Log in',  person='COWNER'):
        driver = self.driver
        sign_in = SignInPage(driver)
        header = Header(driver)
        update_company = UpdateCompanyPage(driver)
        my_companies = MyCompaniesPage(driver)

        sign_in.login(person)
        header.select_option(option)

        my_companies.click_my_companies()
        my_companies.click_company_update()
        update_company.update_company_name(CownerData.UPDATE_COMPANY_NAME)
        update_company.click_update_company_button()


