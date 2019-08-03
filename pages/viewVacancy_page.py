from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsViewVacancy


class ViewVacancyPage():

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.wait = WebDriverWait(self.browser.driver, 20)
        self.locators = LocatorsViewVacancy

    def click_sendResume_button(self):
        """This function provides a push of a 'Send Resume' button, which sends a resume to the company"""
        self.browser.click_element_double_locator(self.locators.TEXT, self.locators.SEND_RESUME_BUTTON)

    # def click_showCompany_button(self):
    #     """This function provides a push of a 'Show Company' button, which allows to see details about company"""
    #     self.browser.driver.find_element_by_css_selector(self.showCompany_button_cssSelector).click()
