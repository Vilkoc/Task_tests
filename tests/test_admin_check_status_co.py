from init import BasePage
from pages.companies_page import CompaniesPage
from pages.sign_in_page import SignInPage
import unittest


class TestAdminCheckStatusCo(BasePage):

    @unittest.skip('skip, as password doesnt change')
    def test_admin_check_status_co(self, person='ADMIN'):
        signin = SignInPage(self)
        signin.login(person)
        companies = CompaniesPage(self)
        assert companies.view_status_of_co()
