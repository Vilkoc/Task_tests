from init import BasePage
from pages.search_page import SearchPage


class TestSearch(BasePage):
    """On this page, user can do the search"""

    def test_search_button(self):

        search = SearchPage(self)
        search.search_button_click()

        search.criteria_choose()

        search.key_word_field()

        search.start_search_click()

        assert search.filter_city()