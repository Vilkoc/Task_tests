from locators import LocatorsSearch


class SearchPage():

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsSearch

    def search_button_click(self):
        self.browser.click_element(self.locators.SEARCH)

    def criteria_choose(self):
        self.browser.click_element(self.locators.CRITERIA)

    def key_word_field(self):
        self.browser.click_element(self.locators.KEY_WORD)
        # self.clear_element(self.locators.KEY_WORD, text_value='default')
        self.browser.send_keys(self.locators.KEY_WORD, 'chernivtsi')

    def start_search_click(self):
        self.browser.click_element(self.locators.SEARCH_START)
