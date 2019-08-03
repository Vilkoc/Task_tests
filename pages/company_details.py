from methods import Methods
from locators import LocatorsCompaniesDetailsPage


class CompanyDetailsPage(Methods):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsCompaniesDetailsPage

    def create_claim(self):
        self.click_element(self.locators.CREATE_CLAIM_BTN)

    def send_claim(self):
        self.click_element(self.locators.SEND_CLAIM_BTN)

    def cancel_claim(self):
        self.click_element(self.locators.CANCEL_CLAIM_BTN)

    def select_title_of_claim(self):
        self.c(self.locators.SELECT_TITLE)

    def set_description_of_claim(self):
        self.send_keys(self.locators.CLAIM_DESCRIPTION,"qwerty")
