from methods import Methods
from locators import LocatorsCreateVacancyPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CreateVacancyPage(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LocatorsCreateVacancyPage
        self.wait = WebDriverWait(self.driver, 10)

    def click_create_vacancy(self):
        self.click_element(self.locators.CREATE_VACANCY_BUTTON)

    def enter_vacancy_data(self, vac_data):
        for el in range(len(self.locators.VACANCY_FIELDS)):
            self.send_keys((By.ID, self.locators.VACANCY_FIELDS[el]), vac_data[el])

    def choose_employment(self):
        self.click_element(self.locators.VACANCY_EMPLOYMENT_DROPBOX)

    def choose_currency(self):
        self.click_element(self.locators.VACANCY_CURRRENCY_DROPBOX)

    def click_add_requirement(self):
        self.click_element(self.locators.ADD_REQUIREMENT_BUTTON)

    def enter_requirements(self, req):
        i = 0
        self.click_add_requirement()
        self.wait.until(EC.element_to_be_clickable(self.locators.VAC_REQUIREMENT_TEXTBOX))
        for val in req:
            self.send_keys((By.CSS_SELECTOR, self.locators.VAC_REQUIREMENT_TEXTBOX[i]), req[i])
            i += 1

    def click_vacancy_create(self):
        self.click_element(self.locators.VACANCY_CREATE_BUTTON)
