import time

from init import BasePage
import unittest

from pages.companies_page import CompaniesPage
from pages.header import Header
from pages.sign_in_page import SignInPage


class TestTrial(BasePage):

    def test_login_logout(self, person='ADMIN'):
        driver = self.driver
        start = Header(driver)
        signin = SignInPage(driver)
        companies = CompaniesPage(driver)

        start.transit('Log in')
        signin.login(person)


if __name__ == "__main__":
    unittest.main()
