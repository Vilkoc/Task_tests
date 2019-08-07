from init import SeleniumTestBase
from data_tests.cowner_data import CownerData


class TestDeleteCompany(SeleniumTestBase):

    def test_create_vacancy(self):
        self.header.select_option(CownerData.OPTION)
        self.sign_in_page.login(CownerData.PERSON)

        self.header.click_my_companies()
        self.my_companies_page.click_company_delete(CownerData.COMPANY_DELETE)

        check = self.my_companies_page.check_company_present(CownerData.COMPANY_DELETE)
        assert check
