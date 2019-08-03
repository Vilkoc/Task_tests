from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsVacancies
from methods import Methods


class VacanciesPage(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = LocatorsVacancies

    def click_viewDetails_button(self):
        """This function provides a push of a 'View Details' button, which allows to see details about the vacancy"""
        self.click_element(self.locators.VIEW_DETAILS_BUTTON)
