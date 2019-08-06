from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsPreviewResume


class PreviewResumePage():
    """On this page user or cowner can change infjrmation in resume, send resume, and open resume in new tab"""

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.wait = WebDriverWait(self.browser.driver, 30)
        self.locators = LocatorsPreviewResume

    def click_sendEmail_button(self):
        self.browser.click_element_by_text(self.locators.BUTTONS, 'Send Email')

    def click_change_button(self):
        self.browser.click_one_button(self.locators.BUTTONS, self.locators.RESUME)

    def confirmation_message(self):
        msg = self.browser.pop_up_element(self.locators.MESSAGE).text
        return msg
