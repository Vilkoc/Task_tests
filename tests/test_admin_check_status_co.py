import time

from init import BasePage
import unittest

from pages.companies_page import CompaniesPage
from pages.header import Header



    def test_login_logout(self, person='ADMIN'):
        driver = self.driver
        start = Header(driver)
        signin = SignInPage(driver)
        companies = CompaniesPage(driver)

        start.transit('Log in')
        signin.login(person)
        time.sleep(1)
        for i in companies.view_status_of_co():
            print(i.text)
            print('qwerty')
