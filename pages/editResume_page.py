POSITION_FIELD_ID = 'position'
PREVIEW_PDF_BUTTON_CSS_SELECTOR = 'button[class="btn btn-success"]'
GET_TEXT_FROM_FIELD = 'ng-reflect-model'


class EditResumePage:

    def __init__(self, driver):
        self.driver = driver

        self.position_field_id = POSITION_FIELD_ID
        self.previewPDF_button_cssSelector = PREVIEW_PDF_BUTTON_CSS_SELECTOR
        self.getText_from_field = GET_TEXT_FROM_FIELD

    def change_positionField(self, position):
        x = self.driver.find_element_by_id(self.position_field_id)
        x.click()
        x.clear()
        x.send_keys(position)

    def click_previewPDF_button(self):
        self.driver.find_element_by_css_selector(self.previewPDF_button_cssSelector).click()

    def confirmation_changes(self):
        text = self.driver.find_element_by_id(self.position_field_id).get_attribute(self.getText_from_field)
        return text
