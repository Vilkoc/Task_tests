from selenium.webdriver.support.ui import WebDriverWait
from methods import Methods
from locators import LocatorsViewVacancy


class ViewVacancyPage(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = LocatorsViewVacancy

    def click_sendResume_button(self):
        """This function provides a push of a 'Send Resume' button, which sends a resume to the company"""
        self.click_element_double_locator(self.locators.TEXT, self.locators.SEND_RESUME_BUTTON)

    def click_showCompany_button(self):
        """This function provides a push of a 'Show Company' button, which allows to see details about company"""
        self.driver.find_element_by_css_selector(self.showCompany_button_cssSelector).click()
