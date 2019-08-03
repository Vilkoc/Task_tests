from init import BasePage
from pages.searchPage import SearchPage


class SearchTest(BasePage):

    def test_search_button(self):

        search = SearchPage(self)
        search.search_button_click()

        search.criteria_choose()

        search.key_word_field()

        search.start_search_click()

        # tmp = driver.find_element_by_xpath('//table//td[contains(text(), "Chernivtsi")]').text
        # self.assertEqual(tmp, "Chernivtsi")
        #
        # masive = ['Position', 'Company', 'City', 'Employment', 'Salary']
        # k = masive.index('City')
        # print(k)
