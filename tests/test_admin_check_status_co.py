from init import SeleniumTestBase
from pages.companies_page import CompaniesPage
from pages.sign_in_page import SignInPage


class TestAdminCheckStatusCo(SeleniumTestBase):

    def test_admin_check_status_co(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('ADMIN')

        assert self.companies_page.view_status_of_co()
