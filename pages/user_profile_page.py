from locators import LocatorsUserPage


class UserPage():
    """User Page"""
    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsUserPage


    def enter_data_textbox(self, key, value):
        """Enters into the specific field data and returns True/False for valid/invalid data"""
        self.browser.clear_element(self.locators.user_fields[key])
        self.browser.send_keys(self.locators.user_fields[key], value)
        temp = self.browser.get_attr_value(self.locators.user_fields[key], 'class')
        if 'ng-invalid' in temp:
            return False
        else:
            return True

    def read_data_textbox(self, key):
        return self.browser.get_attr_value(self.locators.user_fields[key], 'ng-reflect-model')

    def click_update_profile(self):
        self.browser.click_element(self.locators.UPDATE_PROFILE)