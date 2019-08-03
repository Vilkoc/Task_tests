from methods import Methods
from locators import LocatorsSearch


class SearchPage(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsSearch

    def search_button_click(self):
        self.click_element(self.locators.SEARCH)

    def criteria_choose(self):
        self.click_element(self.locators.CRITERIA)

    def key_word_field(self):
        self.click_element(self.locators.KEY_WORD)
        # self.clear_element(self.locators.KEY_WORD, text_value='default')
        self.send_keys(self.locators.KEY_WORD, 'chernivtsi')

    def start_search_click(self):
        self.click_element(self.locators.SEARCH_START)
