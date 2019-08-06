from locators import LocatorsSearch
from data_tests import guest_data


class SearchPage():
    """On this page users can do search"""

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsSearch

    def search_button_click(self):
        self.browser.click_element(self.locators.SEARCH)

    def criteria_choose(self):
        self.browser.click_element(self.locators.CRITERIA)

    def key_word_field(self):
        self.browser.click_element(self.locators.KEY_WORD)
        self.browser.send_keys(self.locators.KEY_WORD, guest_data.CHERNIVTSI)

    def start_search_click(self):
        self.browser.click_element(self.locators.SEARCH_START)

    def filter_city(self):
        tbody = self.browser.get_elements(self.locators.FILTER_CITY)
        for i in tbody:
            if "Chernivtsi" in i.text:
                return True
