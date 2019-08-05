from locators import LocatorsViewCompanyPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import TIMEOUT

class ViewCompanyPage():
    """On this page company owner can look through company information, create vacancies,
     view ther details and close/re-open them"""

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsViewCompanyPage
        self.wait = WebDriverWait(base_obj.browser.driver, TIMEOUT)

    def click_create_vacancy(self):
        self.browser.click_element(self.locators.CREATE_VACANCY_BUTTON)

    def view_vacancy_details(self, vacancy_name):
        self.wait.until(EC.element_to_be_clickable(self.locators.VACANCY_DETAILS_BUTTON))
        card = self.browser.get_elements(self.locators.SIMPLE_VACANCY_DIV)
        for i in card:
            if vacancy_name in i.text:
                td = i.find_element(*self.locators.VACANCY_DETAILS_BUTTON)
                td.click()
