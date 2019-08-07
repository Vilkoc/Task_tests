from init import SeleniumTestBase
from data_tests.user_data import user_data_rab_19 as entry


class TestNamePositive(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read and valid_entry

    def test_first_name(self, field='FIRST_NAME'):
        self.routine(field)

    def test_last_name(self, field='LAST_NAME'):
        self.routine(field)

    def tearDown(self):
        self.header.select_option('Log out')


class TestContactsPositive(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read and valid_entry

    def test_email(self, field='EMAIL'):
        self.routine(field)

    def test_phone(self, field='PHONE'):
        self.routine(field)

    def tearDown(self):
        self.header.select_option('Log out')


# class TestAddressPositive(SeleniumTestBase):
#
#     def setUp(self):
#         self.header.select_option('Log in')
#         self.sign_in_page.login('USER')
#         self.header.select_option('Profile')
#
#     def routine(self, field):
#         valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
#         self.user_profile_page.click_update_profile()
#         read = self.user_profile_page.read_data_textbox(field)
#         assert entry[field] == read and valid_entry
#
#     def test_country(self, field='COUNTRY'):
#         self.routine(field)
#
#     def test_city(self, field='CITY'):
#         self.routine(field)
#
#     def test_street(self, field='STREET'):
#         self.routine(field)
#
#     def test_building(self, field='BUILDING'):
#         self.routine(field)
#
#     def test_zip_code(self, field='ZIP_CODE'):
#         self.routine(field)
#
#     def tearDown(self):
#         self.header.select_option('Log out')


