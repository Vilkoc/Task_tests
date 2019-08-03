import unittest

from basepage import BasePage
from pages.companies_page import CompaniesPage
from pages.sign_in_page import SignInPage


class TestAdmin(BasePage):

    def test_login_logout(self, person='ADMIN'):
        driver = self.driver
        signin = SignInPage(driver)
        signin.login(person)
        companies = CompaniesPage(driver)
        companies.view_detail_about_co()


if __name__ == "__main__":
    unittest.main()
