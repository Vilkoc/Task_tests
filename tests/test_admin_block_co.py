import unittest
from init import BasePage
from pages.companies_page import CompaniesPage
from pages.sign_in_page import SignInPage


class TestAdminBlockCo(BasePage):

    @unittest.skip('skip due to: "https://ssu-jira.softserveinc.com/browse/RAB-86"')
    class TestTrial(BasePage):

        def test_block_co(self, person='ADMIN'):
            signin = SignInPage(self)
            signin.login(person)
            companies = CompaniesPage(self)
            companies.block_co()
            assert companies.confirm_with_popup() == "Company blocked"

