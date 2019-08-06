from init import SeleniumTestBase
from data_tests.user_data import user_data_rab_19 as entry


class TestNamePositive(SeleniumTestBase):

    def setUp(self):
        self.sign_in_page.login("USER")
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read and valid_entry

    def test_first_name(self, field='FIRST_NAME'):
        self.routine(field)


    def tearDown(self):
        self.header.select_option('Log out')


