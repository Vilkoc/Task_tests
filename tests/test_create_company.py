from init import BasePage
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.create_company_page import CreateCompanyPage
from test_data import CownerData
import time


class TestCreateCompany(BasePage):

    def test_create_company(self, option='Log in',  person='COWNER'):
        driver = self.driver
        sign_in = SignInPage(driver)
        header = Header(driver)
        create_company = CreateCompanyPage(driver)

        header.select_option(option)
        sign_in.login(person)

        create_company.click_create_company_at_navbar()
        create_company.enter_data(CownerData.COMPANY_DATA)
        create_company.click_create_button()
        create_company.click_mycompanies_at_navbar()

        comp = self.driver.find_elements_by_xpath(
            "//table//td[contains(text(),'ShevaCo') and string-length(normalize-space(text()))<8]")
        self.assertTrue(comp)


