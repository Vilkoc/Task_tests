import time

from methods import Methods
from locators import LocatorsHeader
from config import PAUSE


class Header(Methods):
    """Header page, which will be inherited by other pages"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsHeader

    def click_icon(self):
        """Clicks on the round icon"""
        self.pause(PAUSE)
        self.click_element(self.locators.ICON)

    def click_log_out(self):
        """Clicks on the round icon"""
        self.click_element_by_text_simple(self.locators.LOG_OUT)

    def click_log_in(self):
        """Clicks on the round icon"""
        self.click_element_by_text_simple(self.locators.LOG_IN)

    def is_logined(self):
        """ Check if user logined: if 'logout' button exist == logined """
        self.click_icon()
        # time.sleep(5) #==========================
        log_out = self.get_elements_by_text(self.locators.LOG_OUT)
        # return log_out.text == TEXT.LOG_OUT
        # time.sleep(3) #test <<<<<<<<<<<<<<<<<<
        return log_out.text == 'Log out'

    def select_option(self, pick_item):
        """The pick_item is default string parameter which accepts only 'Log in', 'Profile', 'Log out' values"""
        values = ('Log in', 'Profile', 'Log out')
        if pick_item not in values:
            raise Exception('Incorrect value for click_dropdown function')
        self.click_element_by_text(self.locators.DROPDOWN, pick_item)

    def transit(self, pick_item):
        self.click_icon()
        self.select_option(pick_item)

