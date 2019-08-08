from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsPreviewResume


class PreviewResumePage():
    """On this page user or cowner can change infjrmation in resume, send resume, and open resume in new tab"""

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser.driver, 30)
        self.locators = LocatorsPreviewResume

    def click_sendEmail_button(self):
        self.browser.click_element_by_text(self.locators.BUTTONS, 'Send Email')

    def click_change_button(self):
        self.browser.click_button_change(self.locators.BUTTONS, self.locators.RESUME)

    def confirmation_message(self):
        self.browser.driver.execute_script("window.scrollTo(0, 0);")
        msg = self.browser.pop_up_element(self.locators.MESSAGE).text
        return msg
