from init import BasePage
import unittest

from pages.companies_page import CompaniesPage
from pages.sign_in_page import SignInPage


class TestTrial(BasePage):

    def test_login_logout(self, person='ADMIN'):
        driver = self.driver
        signin = SignInPage(driver)
        signin.login(person)
        companies = CompaniesPage(driver)

        for i in companies.view_status_of_co():
            print(i.text)
            print('qwerty')


