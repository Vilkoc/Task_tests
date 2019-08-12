from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsViewCompany


class ViewCompanyPage:
    """On this page users can view all vacancies of this company"""
    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.wait = WebDriverWait(self.browser.driver, 20)
        self.locators = LocatorsViewCompany

    def click_claim_button(self):
        self.browser.click_element(self.locators.CLAIM_BUTTON)

    def choose_option(self):
        self.browser.click_element(self.locators.TITLE)

    def fill_out_description_field(self, text):
        self.browser.send_keys(self.locators.DESCRIPTION_FIELD, text)

    def wait_invisibility_of_element(self):
        self.browser.invisibility_of_element(self.locators.SEND_CLAIM_BUTTON)

    def click_send_claim_button(self):
        self.browser.click_element(self.locators.SEND_CLAIM_BUTTON)
        self.wait_invisibility_of_element()


