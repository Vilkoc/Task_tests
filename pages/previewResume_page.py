from selenium.webdriver.support.ui import WebDriverWait
from locators import LocatorsPreviewResume


class PreviewResumePage():

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.wait = WebDriverWait(self.browser.driver, 30)
        self.locators = LocatorsPreviewResume

    def click_sendEmail_button(self):
        """This function provides a push of a 'Send Email' button"""
        self.browser.click_element_by_text(self.locators.BUTTONS, 'Send Email')

    def click_change_button(self):
        """This function provides a push of a 'Change' button, which allows change information in resume"""
        self.browser.click_one_button(self.locators.BUTTONS, self.locators.RESUME)

    def confirmation_message(self):
        """This function reads the message from the popup window and passes it to the variable"""
        msg = self.browser.pop_up_element(self.locators.MESSAGE).text
        return msg

    # def click_full_pdf_button(self):
    #     self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="form-group"]>iframe')))
    #     buttons = self.driver.find_elements_by_css_selector(self.buttons_cssSelector)
    #     for i in buttons:
    #         if i.text == 'Full PDF':
    #             i.click()
