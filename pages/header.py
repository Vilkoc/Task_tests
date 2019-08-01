from methods import Methods
from locators import LocatorsHeader


class Header(Methods):
    """Header page, which will be inherited by other pages"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsHeader

    def click_icon(self):
        """Clicks on the round icon"""
        self.click_element(self.locators.ICON)

    def check_dropdown(self):
        flag = self.get_attr_value(self.locators.CHECK_DROPDOWN, 'aria-expanded')
        if flag == 'true':
            return True
        else:
            return False

    def select_option(self, pick_item):
        """The pick_item is default string parameter which accepts only 'Log in', 'Profile', 'Log out' values"""
        values = ('Log in', 'Profile', 'Log out')
        if pick_item not in values:
            raise Exception('Incorrect value for click_dropdown function')
        self.click_icon()
        if self.check_dropdown():
            self.click_element_by_text(self.locators.DROPDOWN, pick_item)
        else:
            self.click_icon()
