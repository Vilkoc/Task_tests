from locators import LocatorsCreateVacancyPage
from locators import LocatorsCreateCompanyPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import TIMEOUT


class CreateVacancyPage():
    """On this page company owner can create vacancy after creation of the company"""

    def __init__(self, browser):
        self.locators = LocatorsCreateVacancyPage
        self.loc = LocatorsCreateCompanyPage
        self.browser = browser
        self.wait = WebDriverWait(browser.driver, TIMEOUT)

    def enter_vacancy_data(self, vac_data):
        """Enters into the specific field data"""
        for el in range(len(self.locators.VACANCY_FIELDS)):
            self.browser.send_keys((By.ID, self.locators.VACANCY_FIELDS[el]), vac_data[el])

    def choose_employment(self):
        self.browser.click_element(self.locators.VACANCY_EMPLOYMENT_DROPBOX)

    def choose_currency(self):
        self.browser.click_element(self.locators.VACANCY_CURRRENCY_DROPBOX)

    def click_add_requirement(self):
        self.browser.click_element(self.locators.ADD_REQUIREMENT_BUTTON)

    def enter_requirements(self, req):
        """Enters into the requirement fields data"""
        self.click_add_requirement()
        all_req_fields = self.browser.get_elements(self.locators.VAC_REQUIREMENT_TEXTBOX)
        index_of_textbox = 0
        for req_field in all_req_fields:
            req_field.send_keys(req[index_of_textbox])
            index_of_textbox += 1

    def click_vacancy_create(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.VACANCY_CREATE_BUTTON))
        self.browser.click_element(self.locators.VACANCY_CREATE_BUTTON)

    def read_vacancy_data(self):
        vacancy_data = self.browser.read_data_in_textbox(self.locators.VACANCY_FIELDS,
                                              self.loc.ATTRIBUTE_OF_COMPANIES_VACANCIES_TEXTBOXES)
        return vacancy_data
