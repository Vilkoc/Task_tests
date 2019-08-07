from locators import LocatorsUserPage


class UserPage:
    """User page with user's Profile"""
    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsUserPage

    def clear_data_textbox(self, key):
        """Clears specified textbox"""
        self.browser.clear_element(self.locators.user_fields[key])

    def enter_data_textbox(self, key, value):
        """Enters into the specific field data and returns True/False for valid/invalid data"""
        self.clear_data_textbox(key)
        self.browser.send_keys(self.locators.user_fields[key], value)
        return True if self.check_validity_data(key) else False

    def check_invalidity_data(self, key):
        """Verifies if UI alerts about invalid data input"""
        temp = self.browser.get_attr_value(self.locators.user_fields[key], 'class')
        return True if 'ng-invalid' in temp else False

    def check_validity_data(self, key):
        """Verifies if UI accepts valid data input"""
        temp = self.browser.get_attr_value(self.locators.user_fields[key], 'class')
        return True if 'ng-valid' in temp else False

    def read_data_textbox(self, key):
        """Extracts text data from specified textbox"""
        return self.browser.get_attr_value(self.locators.user_fields[key], 'ng-reflect-model')

    def disabled_update_profile_button(self):
        """Returns True/False if the Update Profile button is disabled/enabled"""
        temp = self.browser.get_property_wrapper(self.locators.UPDATE_PROFILE, 'disabled')
        return True if temp else False

    def click_update_profile(self):
        """Clicks on the Update Profile button"""
        self.browser.click_element(self.locators.UPDATE_PROFILE)
