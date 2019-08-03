from locators import LocatorsMyCompaniesPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import TIMEOUT


class MyCompaniesPage():
    """On this page company owner can look through his all companies, update their info and delete them"""

    def __init__(self, base_obj):
        self.locators = LocatorsMyCompaniesPage
        self.browser = base_obj.browser
        self.wait = WebDriverWait(base_obj.browser.driver, TIMEOUT)

    def click_create_company(self):
        self.browser.click_element(self.locators.CREATE_COMPANY_BUTTON)

    def click_view_details(self):
        self.browser.click_element(self.locators.COMPANY_DETAIL_BUTTON_SOFTSERVE)

    def click_company_update(self):
        self.browser.click_element(self.locators.COMPANY_UPDATE_BUTTON_VALSOFT)

    def click_company_delete(self, company_name):
        self.wait.until(EC.element_to_be_clickable(self.locators.DELETE_COMPANY_BUTTON))
        self.browser.company_view_update_delete(self.locators.TABLE_BODY, self.locators.DELETE_COMPANY_BUTTON,
                                                company_name)

    def check_company_present(self, co_name):
        tbody = self.browser.get_elements(self.locators.TABLE_BODY)
        for i in tbody:
            if co_name not in i.text:
                return True
            else:
                return False
