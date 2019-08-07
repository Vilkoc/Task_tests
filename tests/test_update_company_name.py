from init import SeleniumTestBase
from data_tests.cowner_data import CownerData


class TestUpdateCompanyName(SeleniumTestBase):
    def test_update_company_name(self):
        self.header.select_option(CownerData.OPTION)
        self.sign_in_page.login(CownerData.PERSON)

        self.header.click_my_companies()
        self.my_companies_page.click_update(CownerData.COMPANY_FOR_UDATING)
        self.update_company_page.update_company_name(CownerData.COMPANY_RENAME)
        self.update_company_page.click_update_company_button()
        self.my_companies_page.click_update(CownerData.COMPANY_RENAME)
        co_name = self.update_company_page.check_company_name()
        assert co_name == CownerData.COMPANY_RENAME




