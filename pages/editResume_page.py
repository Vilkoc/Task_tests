from locators import LocatorsEditResume
from methods import Methods



class EditResumePage(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsEditResume

    def change_positionField(self, position):
        # self.click_element_double_locator(self.locators.PREVIEW_PDF_BUTTON, self.locators.POSITION_FIELD)
        # self.clear_element(self.locators.POSITION_FIELD, '')

        position_field = self.driver.find_element(self.locators.POSITION_FIELD)
        position_field.click()
        position_field.clear()
        position_field.send_keys(position)

    # def click_previewPDF_button(self):
    #     self.driver.find_element_by_css_selector(self.previewPDF_button_cssSelector).click()
    #
    # def confirmation_changes(self):
    #     text = self.driver.find_element_by_id(self.position_field_id).get_attribute(self.getText_from_field)
    #     return text
