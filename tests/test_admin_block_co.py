import unittest
from init import BasePage
from pages.companies_page import CompaniesPage
from pages.sign_in_page import SignInPage


class TestAdminBlockCo(BasePage):

    def __init__(self):
        self.signin = SignInPage(self)

    @unittest.skip('skip due to: "https://ssu-jira.softserveinc.com/browse/RAB-86"')
    def test_block_co(self, person='ADMIN'):

        self.signin.login(person)
        companies = CompaniesPage(self)
        companies.block_co()
        assert companies.confirm_with_popup() == "Company blocked"
