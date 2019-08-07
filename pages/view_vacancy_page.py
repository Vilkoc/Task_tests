from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsViewVacancy


class ViewVacancyPage():
    """On this page users can return to all vacancies page, view info about company, and go to preview resume"""
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser.driver, 20)
        self.locators = LocatorsViewVacancy

    def click_sendResume_button(self):
        self.browser.click_element_double_locator(self.locators.TEXT, self.locators.SEND_RESUME_BUTTON)

    def click_showCompany_button(self):
        self.browser.click_element(self.locators.SHOW_COMPANY_BUTTON)