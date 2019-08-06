from locators import LocatorsCreateVacancyPage
from locators import LocatorsCreateCompanyPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import TIMEOUT


class CreateVacancyPage():
    """On this page company owner can create vacancy after creation of the company"""

    def __init__(self, base_obj):
        self.locators = LocatorsCreateVacancyPage
        self.loc = LocatorsCreateCompanyPage
        self.browser = base_obj.browser
        self.wait = WebDriverWait(base_obj.browser.driver, TIMEOUT)

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
        a = self.browser.get_elements(self.locators.VAC_REQUIREMENT_TEXTBOX)
        c = 0
        for i in a:
            i.send_keys(req[c])
            c += 1

    def click_vacancy_create(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.VACANCY_CREATE_BUTTON))
        self.browser.click_element(self.locators.VACANCY_CREATE_BUTTON)

    def read_vacancy_data(self):
        z = self.browser.read_data_in_textbox(self.locators.VACANCY_FIELDS,
                                              self.loc.ATTRIBUTE_OF_COMPANIES_VACANCIES_TEXTBOXES)
        return z
