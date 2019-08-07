from init import SeleniumTestBase
from data_tests.cowner_data import CownerData
import time


class TestCreateCompany(SeleniumTestBase):

    def test_create_company(self):
        self.header.select_option(CownerData.OPTION)
        self.sign_in_page.login(CownerData.PERSON)

        self.header.click_create_company()
        self.create_company_page.enter_data(CownerData.COMPANY_DATA)
        self.create_company_page.click_create_button()
        self.header.click_my_companies()
        self.my_companies_page.click_update(CownerData.COMPANY_CREATE)
        company_data = self.create_company_page.read_data()

        num_of_data = 0
        for data in CownerData.COMPANY_DATA:
            assert data == company_data[num_of_data]
            num_of_data += 1
