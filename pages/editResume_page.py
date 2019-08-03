from locators import LocatorsEditResume


class EditResumePage():

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsEditResume

    def change_positionField(self, position):
        self.browser.clear_element(self.locators.POSITION_FIELD)
        self.browser.send_keys(self.locators.POSITION_FIELD, position)

    def click_previewPDF_button(self):
        self.browser.click_element(self.locators.PREVIEW_PDF_BUTTON)

    def confirmation_changes(self):
        text = self.browser.get_attr_value(self.locators.POSITION_FIELD, self.locators.GET_TEXT_FROM_FIELD)
        return text
