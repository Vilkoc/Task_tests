from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsViewCompany


class ViewCompanyPage:

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.wait = WebDriverWait(self.browser.driver, 20)
        self.locators = LocatorsViewCompany

    def click_claim_button(self):
        """This function provides a push of a 'Claim' button, which opens the fields 'Title' and 'Description'"""
        self.browser.click_element(self.locators.CLAIM_BUTTON)

    def choose_option(self):
        """This function select option from drop down list, for 'Title' field"""
        self.browser.click_element(self.locators.TITLE)

    def fill_out_description_field(self, text):
        """This function fill out 'Description' field"""
        self.browser.send_keys(self.locators.DESCRIPTION_FIELD, text)

    def wait_invisibility_of_element(self):
        """This function wait until button 'Send claim' will be invisible"""
        self.browser.invisibility_of_element(self.locators.SEND_CLAIM_BUTTON)

    def click_send_claim_button(self):
        """This function provides a push of a 'Claim' button, which sends the claim to the company"""
        self.browser.click_element(self.locators.SEND_CLAIM_BUTTON)
        self.wait_invisibility_of_element()


