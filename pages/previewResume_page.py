BUTTONS_CSS_SELECTOR = 'button[class="btn btn-success"]'
MESSAGE_CSS_SELECTOR = 'div[class="wrap"]>p'


class PreviewResumePage:

    def __init__(self, driver):
        self.driver = driver

        self.buttons_cssSelector = BUTTONS_CSS_SELECTOR
        self.message_cssSelector = MESSAGE_CSS_SELECTOR

    def click_sendEmail_button(self):
        buttons = self.driver.find_elements_by_css_selector(self.buttons_cssSelector)
        send_email = None
        for i in buttons:
            if i.text == 'Send Email':
                send_email = i
        return send_email.click()

    def click_change_button(self):
        buttons = self.driver.find_elements_by_css_selector(self.buttons_cssSelector)
        change = None
        for i in buttons:
            if i.text == 'Change':
                change = i
        return change.click()

    def confirmation_message(self):
        msg = self.driver.find_element_by_css_selector(self.message_cssSelector).text
        return msg
