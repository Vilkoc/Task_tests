from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsVacancies


class VacanciesPage():
    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.wait = WebDriverWait(self.browser.driver, 20)
        self.locators = LocatorsVacancies

    def click_viewDetails_button(self):
        """This function provides a push of a 'View Details' button, which allows to see details about the vacancy"""
        self.browser.click_element(self.locators.VIEW_DETAILS_BUTTON)
