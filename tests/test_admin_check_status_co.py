import time

from init import BasePage

from pages.companies_page import CompaniesPage
from pages.sign_in_page import SignInPage


class TestAdminCheckStatusCo(BasePage):

    def test_login_logout(self, person='ADMIN'):
        signin = SignInPage(self)
        signin.login(person)
        companies = CompaniesPage(self)
        assert companies.view_status_of_co()



