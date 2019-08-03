import unittest
from init import BasePage
from pages.companies_page import CompaniesPage
from pages.sign_in_page import SignInPage


class CreateClaim(BasePage):

    @unittest.skip('skip due to: "https://ssu-jira.softserveinc.com/browse/RAB-86"')
    class TestTrial(BasePage):

        def test_block_co(self, person='ADMIN'):
            driver = self.driver
            signin = SignInPage(driver)
            signin.login(person)
            companies = CompaniesPage(driver)
            companies.block_co()
            self.assertEqual(companies.confirm_with_popup(), "Company blocked")


if __name__ == '__main__':
    unittest.main()
