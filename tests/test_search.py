from init import SeleniumTestBase


class TestSearch(SeleniumTestBase):
    """On this page, user can do the search"""

    def test_search_button(self):

        self.search_page.search_button_click()

        self.search_page.criteria_choose()

        self.search_page.key_word_field()

        self.search_page.start_search_click()

        assert self.search_page.filter_city()
