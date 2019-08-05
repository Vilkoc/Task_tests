from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsVacancies


class VacanciesPage():
    """On this page user or cowner can view vacancies"""
    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.wait = WebDriverWait(self.browser.driver, 20)
        self.locators = LocatorsVacancies

    def click_viewDetails_button(self):
        self.browser.click_element(self.locators.VIEW_DETAILS_BUTTON)
