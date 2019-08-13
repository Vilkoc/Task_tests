from locators import LocatorsViewCompany


class CompanyDetailsPage():
    """Page with details about company and interaction with it"""

    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsViewCompany

    def create_claim(self):
        self.browser.click_element(self.locators.CLAIM_BUTTON)

    def send_claim(self):
        self.browser.click_element(self.locators.SEND_CLAIM_BUTTON)

    def cancel_claim(self):
        self.browser.click_element(self.locators.CANCEL_CLAIM_BTN)

    def select_title_of_claim(self):
        self.browser.click_element(self.locators.TITLE)

    def set_description_of_claim(self):
        self.browser.send_keys(self.locators.DESCRIPTION_FIELD, self.locators.DESCRIPTION_OF_CLAIM)
