from init import BasePage
import unittest
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.create_company_page import CreateCompanyPage
from test_data import CownerData
import time


class TestCreateCompany(BasePage):

    def test_create_company(self, person='COWNER'):
        driver = self.driver
        start = Header(driver)
        signin = SignInPage(driver)

        start.transit('Log in')

        signin.login(person)

        create_company = CreateCompanyPage(driver)
        time.sleep(1)
        create_company.click_create_company_at_navbar()
        create_company.enter_data(CownerData.COMPANY_DATA)
        create_company.click_create_button()
        create_company.click_mycompanies_at_navbar()

        comp = self.driver.find_elements_by_xpath(
            "//table//td[contains(text(),'ShevaCo') and string-length(normalize-space(text()))<8]")
        # self.assertTrue(comp)


if __name__ == "__main__":
    unittest.main()