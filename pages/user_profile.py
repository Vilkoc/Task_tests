from methods import Methods
from locators import Locators, LocatorsUsers
from pages.home_page import HomePage

class UserProfilePage(HomePage):
    """Inherits click_icon method from HomePage"""
    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)
        self.locators = Locators
        self.locator_fields = LocatorsUsers

    def click_profile(self):
        self.click_dropdown('Log in')

    def click_logout(self):
        try:
            self.click_dropdown(1)
        except:
            self.click_icon()
            self.click_dropdown(1)


    # def enter_user_data(self, key_id, data_entry):
    #     try:
    #         self.methods.clear_element(self.locator_fields.
    #         element.clear()
    #         element.send_keys(data_entry)
    #         if 'ng-invalid' in element.get_attribute('class'):
    #             return False
    #         else:
    #             return True
