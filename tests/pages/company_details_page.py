from locators import LocatorsCompaniesDetailsPage


class CompanyDetailsPage():
    """Page with details about company and interaction with it"""

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsCompaniesDetailsPage

    def create_claim(self):
        self.browser.click_element(self.locators.CREATE_CLAIM_BTN)

    def send_claim(self):
        self.browser.click_element(self.locators.SEND_CLAIM_BTN)

    def cancel_claim(self):
        self.browser.click_element(self.locators.CANCEL_CLAIM_BTN)

    def select_title_of_claim(self):
        self.browser.click_element(self.locators.SELECT_TITLE)

    def set_description_of_claim(self):
        self.browser.send_keys(self.locators.CLAIM_DESCRIPTION, self.locators.DESCRIPTION_OF_CLAIM)
