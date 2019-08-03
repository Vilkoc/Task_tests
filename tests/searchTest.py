from init import BasePage
from pages.searchPage import SearchPage


class SearchTest(BasePage):

    def test_search_button(self):
        driver = self.driver

        search = SearchPage(driver)
        search.search_button_click()

        criteria = SearchPage(driver)
        criteria.criteria_choose()

        key_word = SearchPage(driver)
        key_word.key_word_field()

        start = SearchPage(driver)
        start.start_search_click()

        # tmp = driver.find_element_by_xpath('//table//td[contains(text(), "Chernivtsi")]').text
        # self.assertEqual(tmp, "Chernivtsi")
        #
        # masive = ['Position', 'Company', 'City', 'Employment', 'Salary']
        # k = masive.index('City')
        # print(k)
