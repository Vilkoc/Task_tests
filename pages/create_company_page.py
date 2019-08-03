from locators import LocatorsCreateCompanyPage, LocatorsMyCompaniesPage
from selenium.webdriver.common.by import By


class CreateCompanyPage():
    """On this page company owner can create his/her own company"""

    def __init__(self, base_obj):
        self.locators = LocatorsCreateCompanyPage
        self.loc = LocatorsMyCompaniesPage
        self.browser = base_obj.browser

    def enter_data(self, co_data):
        """Enters into the specific field data"""
        for el in range(len(self.locators.COMPANY_FIELDS)):
            self.browser.send_keys((By.ID, self.locators.COMPANY_FIELDS[el]), co_data[el])

    def click_create_button(self):
        self.browser.click_element(self.locators.COMPANY_CREATE_BUTTON)

    def click_update(self, company_name):
        self.browser.company_view_update_delete(self.loc.TABLE_BODY, self.loc.COMPANY_UPDATE_BUTTON, company_name)

    def read_data_textbox(self):
        co_list = []
        for el in range(len(self.locators.COMPANY_FIELDS)):
            a = self.browser.driver.find_element_by_id(self.locators.COMPANY_FIELDS[el]).get_attribute('ng-reflect-model')
            co_list.append(a)
        return co_list
