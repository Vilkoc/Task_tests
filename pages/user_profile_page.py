from methods import Methods
from pages.header import Header
from locators import LocatorsUserPage


class UserPage(Methods):
    """User Page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsUserPage

    def transmit(self, pick_item):
        return Header(self.driver).select_option(pick_item)

    def enter_data_textbox(self, key, value):
        """Enters into the specific field data and returns True/False for valid/invalid data"""
        self.clear_element(self.locators.user_fields[key])
        self.send_keys(self.locators.user_fields[key], value)
        temp = self.get_attr_value(self.locators.user_fields[key], 'class')
        if 'ng-invalid' in temp:
            return False
        else:
            return True

    def read_data_textbox(self, key):
        return self.get_attr_value(self.locators.user_fields[key], 'ng-reflect-model')

    def click_update_profile(self):
        self.click_element(self.locators.UPDATE_PROFILE)
