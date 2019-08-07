from locators import LocatorsViewCompany
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import TIMEOUT


class ViewCompanyPage():
    """On this page company owner can look through company information, create vacancies,
     view their details and close/re-open them"""

    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsViewCompany
        self.wait = WebDriverWait(browser.driver, TIMEOUT)

    def click_create_vacancy(self):
        self.browser.click_element(self.locators.CREATE_VACANCY_BUTTON)

    def view_vacancy_details(self, vacancy_name):
        self.wait.until(EC.element_to_be_clickable(self.locators.VACANCY_DETAILS_BUTTON))
        card = self.browser.get_elements(self.locators.SIMPLE_VACANCY_DIV)
        for element in card:
            if vacancy_name in element.text:
                td = element.find_element(*self.locators.VACANCY_DETAILS_BUTTON)
                td.click()

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
