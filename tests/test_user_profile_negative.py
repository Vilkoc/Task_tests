from init import SeleniumTestBase
from data_tests.user_data import user_data_rab_26 as entry
import unittest
from config import URL


# class TestNameNegative(SeleniumTestBase):
#
#     def setUp(self):
#         self.header.select_option('Log in')
#         self.sign_in_page.login('USER')
#         self.header.select_option('Profile')
#
#     def routine(self, field):
#         valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
#         button_disabled = self.user_profile_page.disabled_update_profile_button()
#         assert not valid_entry and button_disabled
#
#     def test_first_name(self, field='FIRST_NAME'):
#         self.routine(field)
#
#     def test_last_name(self, field='LAST_NAME'):
#         self.routine(field)
#
#     def tearDown(self):
#         self.header.select_option('Log out')


# class TestContactsNegative(SeleniumTestBase):
#
#     def setUp(self):
#         self.header.select_option('Log in')
#         self.sign_in_page.login('USER')
#         self.header.select_option('Profile')
#
#     def routine(self, field):
#         valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
#         button_disabled = self.user_profile_page.disabled_update_profile_button()
#         assert not valid_entry and button_disabled
#
#     @unittest.skip("skip due to bug according to 'https://ssu-jira.softserveinc.com/browse/RAB-80'")
#     def test_email(self, field='EMAIL'):
#         self.routine(field)
#
#     def test_phone(self, field='PHONE'):
#         self.routine(field)
#
#     def tearDown(self):
#         self.header.select_option('Log out')


class TestAddressNegative(SeleniumTestBase):
    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        print('Entered', field)
        button_disabled = self.user_profile_page.disabled_update_profile_button()
        assert not valid_entry and button_disabled

    def test_country(self, field='COUNTRY'):
        self.routine(field)

    def test_city(self, field='CITY'):
        self.routine(field)

    def test_street(self, field='STREET'):
        self.routine(field)

    def test_building(self, field='BUILDING'):
        self.routine(field)

    def test_zip_code(self, field='ZIP_CODE'):
        self.routine(field)

    def tearDown(self):
        self.header.select_option('Log out')
