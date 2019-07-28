SEND_RESUME_BUTTON_CSS_SELECTOR = 'a[class="btn btn-success"]'


class ViewVacancyPage:

    def __init__(self, driver):
        self.driver = driver

        self.sendResume_button_cssSelector = SEND_RESUME_BUTTON_CSS_SELECTOR

    def click_sendResume_button(self):
        self.driver.find_element_by_css_selector(self.sendResume_button_cssSelector).click()
