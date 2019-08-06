from init import BasePage
from pages.user_profile_page import UserPage
from data_tests.user_data import user_data_rab_19 as entry



class TestNamePositive(BasePage):

    def setUp(self):
        self.login(person="USER")
        self.perform = UserPage()
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        self.perform.click_update_profile()
        read = self.perform.read_data_textbox(field)
        assert entry[field] == read and valid_entry

    def test_first_name(self, field='FIRST_NAME'):
        self.routine(field)


    def tearDown(self):
        self.header.select_option('Log out')


