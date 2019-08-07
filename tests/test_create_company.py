from init import SeleniumTestBase
from data_tests.cowner_data import CownerData


class TestCreateCompany(SeleniumTestBase):

    def test_create_company(self):
        self.header.select_option(CownerData.OPTION)
        self.sign_in_page.login(CownerData.PERSON)

        self.header.click_create_company()
        self.create_company_page.enter_data(CownerData.COMPANY_DATA)
        self.create_company_page.click_create_button()
        self.header.click_my_companies()
        self.my_companies_page.click_update(CownerData.COMPANY_CREATE)
        z = self.create_company_page.read_data()

        j = 0
        for i in CownerData.COMPANY_DATA:
            assert i == z[j]
            j += 1
