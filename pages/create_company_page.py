from methods import Methods
from locators import LocatorsCreateCompanyPage, LocatorsMyCompaniesPage
from selenium.webdriver.common.by import By

class CreateCompanyPage(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LocatorsCreateCompanyPage
        self.loc = LocatorsMyCompaniesPage

    def click_create_company_at_navbar(self):
        self.click_element(self.locators.CREATE_COMPANY_TAB)

    def enter_data(self, co_data):
        for el in range(len(self.locators.COMPANY_FIELDS)):
            self.send_keys((By.ID, self.locators.COMPANY_FIELDS[el]), co_data[el])

    def click_create_button(self):
        self.click_element(self.locators.COMPANY_CREATE_BUTTON)

    def click_mycompanies_at_navbar(self):
        self.click_element(self.loc.MY_COMPANIES)

