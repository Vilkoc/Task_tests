from init import BasePage
import unittest

from pages.companies_page import CompaniesPage
from pages.company_details import CompanyDetailsPage
from pages.sign_in_page import SignInPage


class TestTrial(BasePage):

    def test_login_logout(self, person='ADMIN'):
        driver = self.driver
        signin = SignInPage(driver)
        signin.login(person)
        companies = CompaniesPage(driver)
        companies.view_detail_about_co()
        details = CompanyDetailsPage(driver)
        details.select_title_of_claim()
        details.
if __name__ == "__main__":
    unittest.main()
