from init import BasePage
from pages.sign_in_page import SignInPage
from pages.create_company_page import CreateCompanyPage
from test_data import CownerData
import time


class TestCreateCompany(BasePage):

    def test_create_company(self, option='Log in', person='COWNER'):
        sign_in = SignInPage(self)
        create_company = CreateCompanyPage(self)

        self.header.select_option(option)
        sign_in.login(person)

        self.header.click_create_company()
        create_company.enter_data(CownerData.COMPANY_DATA)
        create_company.click_create_button()
        self.header.click_my_companies()
        time.sleep(2)
        create_company.click_update("ShevaCo")
        time.sleep(2)
        z = create_company.read_data_textbox()
        j = 0
        for i in CownerData.COMPANY_DATA:
            assert i == z[j]
            j += 1
