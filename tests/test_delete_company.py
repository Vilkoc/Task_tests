from init import SeleniumTestBase
from pages.my_companies_page import MyCompaniesPage
from data_tests.cowner_data import CownerData


class TestDeleteCompany(SeleniumTestBase):

    def test_create_vacancy(self):
        delete_company = MyCompaniesPage(self)

        self.header.select_option(CownerData.OPTION)
        self.sign_in_page.login(CownerData.PERSON)

        self.header.click_my_companies()
        delete_company.click_company_delete(CownerData.COMPANY_DELETE)

        check = delete_company.check_company_present(CownerData.COMPANY_DELETE)
        assert check
