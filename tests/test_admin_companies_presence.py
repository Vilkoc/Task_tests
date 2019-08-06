import time

from init import BasePage
from pages.companies_page import CompaniesPage
from pages.sign_in_page import SignInPage


class TestAdmin(BasePage):

    @unittest.skip('skip, as password doesnt change')
    def test_admin_companies_presence(self, person='ADMIN'):
        signin = SignInPage(self)
        signin.login(person)
        companies = CompaniesPage(self)
        assert companies.companies_are_visible()
