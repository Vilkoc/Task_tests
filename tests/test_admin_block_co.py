import unittest
from init import SeleniumTestBase
from pages.companies_page import CompaniesPage
from pages.sign_in_page import SignInPage


class TestAdminBlockCo(SeleniumTestBase):

    @unittest.skip('skip due to: "https://ssu-jira.softserveinc.com/browse/RAB-86"')
    def test_block_co(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('ADMIN')

        self.companies_page.block_co()

        assert self.companies_page.confirm_with_popup() == "Company blocked"
