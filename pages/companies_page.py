from methods import Methods
from locators import LocatorsCompaniesPage


class CompaniesPage(Methods):
    """On this page admin can moderate companies"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsCompaniesPage

    def view_detail_about_co(self):
        self.click_element(self.locators.DETAILS_ABOUT_CO)

    def view_status_of_co(self):
        tmp = self.get_elements(self.locators.STATUS_OF_CO)
        return tmp

    def block_co(self):
        self.click_element(self.locators.BLOCK_1_CO)

    def unblock_co(self):
        self.click_element(self.locators.UNBLOCK_2_CO)