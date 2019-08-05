from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsCompaniesPage


class CompaniesPage():
    """On this page admin can moderate companies"""

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.wait = WebDriverWait(self.browser.driver, 20)
        self.locators = LocatorsCompaniesPage

    def view_detail_about_co(self):
        self.browser.click_element(self.locators.DETAILS_ABOUT_CO)

    def view_status_of_co(self):
        tmp = self.browser.get_elements(self.locators.STATUS_OF_CO)
        return tmp

    def block_co(self):
        self.browser.click_element(self.locators.BLOCK_1_CO)

    def unblock_co(self):
        self.browser.click_element(self.locators.UNBLOCK_2_CO)

    def click_show_claims_button(self):
        self.browser.driver.execute_script("window.scrollTo(0, 0);")
        self.browser.click_element(self.locators.SHOW_CLAIMS_BUTTON)

    def description(self):
        element = self.browser.get_elements(self.locators.DESCRIPTION)
        description = None
        for i in element:
            if i.text == 'Text':
                description = i.text
        return description
