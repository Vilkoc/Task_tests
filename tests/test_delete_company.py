from init import BasePage
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.my_companies_page import MyCompaniesPage
from test_data import CownerData
import time


class TestDeleteCompany(BasePage):

    def test_create_vacancy(self, option='Log in', person='COWNER'):
        driver = self.driver
        sign_in = SignInPage(driver)
        header = Header(driver)
        delete_company = MyCompaniesPage(driver)

        header.select_option(option)
        sign_in.login(person)

        delete_company.click_my_companies()
        time.sleep(2)
        delete_company.click_company_delete(CownerData.UPDATE_COMPANY_NAME)
        time.sleep(2)