from locators import LocatorsUserPage


class UserPage():
    """User Page"""
    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsUserPage

    def check_invalidity_data(self, key):
        temp = self.browser.get_attr_value(self.locators.user_fields[key], 'class')
        return True if 'ng-invalid' in temp else False

    def check_validity_data(self, key):
        temp = self.browser.get_attr_value(self.locators.user_fields[key], 'class')
        return True if 'ng-valid' in temp else False

    def clear_data_textbox(self, key):
        self.browser.clear_element(self.locators.user_fields[key])

    def enter_data_textbox(self, key, value):
        """Enters into the specific field data and returns True/False for valid/invalid data"""
        self.clear_data_textbox(key)
        self.browser.send_keys(self.locators.user_fields[key], value)
        return True if self.check_validity_data(key) else False

    def read_data_textbox(self, key):
        return self.browser.get_attr_value(self.locators.user_fields[key], 'ng-reflect-model')

    def disabled_update_profile_button(self):
        """Returns True if the button is disabled"""
        temp = self.browser.get_property_wrapper(self.locators.UPDATE_PROFILE, 'disabled')
        return True if temp else False

    def click_update_profile(self):
        self.browser.click_element(self.locators.UPDATE_PROFILE)




