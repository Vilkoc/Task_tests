from methods import Methods
from locators import LocatorsMyCompaniesPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import TIMEOUT
import time


class MyCompaniesPage(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LocatorsMyCompaniesPage
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def click_my_companies(self):
        self.click_element(self.locators.MY_COMPANIES)

    def click_create_company(self):
        self.click_element(self.locators.CREATE_COMPANY_BUTTON)

    def click_view_details(self):
        self.click_element(self.locators.COMPANY_DETAIL_BUTTON_SOFTSERVE)

    def click_company_update(self):
        self.click_element(self.locators.COMPANY_UPDATE_BUTTON_SHEVACO)

    def click_company_delete(self, company_name):
        self.companies(self.locators.TABLE_BODY, self.locators.DELETE_COMPANY_BUTTON, company_name)




