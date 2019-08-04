from locators import LocatorsEditResume


class EditResumePage():

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsEditResume

    def change_positionField(self, position):
        """This function clears 'Position' field and then fill out him"""
        self.browser.clear_element(self.locators.POSITION_FIELD)
        self.browser.send_keys(self.locators.POSITION_FIELD, position)

    def click_previewPDF_button(self):
        """This function clicks on 'Preview PDF' button"""
        self.browser.click_element(self.locators.PREVIEW_PDF_BUTTON)

    def confirmation_changes(self):
        """This function takes value from 'Position' field"""
        text = self.browser.get_attr_value(self.locators.POSITION_FIELD, self.locators.GET_TEXT_FROM_FIELD)
        return text
