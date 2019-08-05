from init import BasePage
from pages.sign_in_page import SignInPage
from pages.user_profile_page import UserPage
from data_tests.user_data import user_data_rab_26 as entry
from config import URL
import unittest


class TestNameNegative(BasePage):

    def setUp(self):
        self.browser.driver.get(URL)
        start = SignInPage(self)
        self.perform = UserPage(self)
        start.login('USER')
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        button_disabled = self.perform.disabled_update_profile_button()
        assert not valid_entry and button_disabled

    def test_first_name(self, field='FIRST_NAME'):
        self.routine(field)

    def test_last_name(self, field='LAST_NAME'):
        self.routine(field)

    def tearDown(self):
        self.header.select_option('Log out')


class TestContactsNegative(BasePage):

    def setUp(self):
        self.browser.driver.get(URL)
        start = SignInPage(self)
        self.perform = UserPage(self)
        start.login('USER')
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        button_disabled = self.perform.disabled_update_profile_button()
        assert not valid_entry and button_disabled

    @unittest.skip("skip due to bug according to 'https://ssu-jira.softserveinc.com/browse/RAB-80'")
    def test_email(self, field='EMAIL'):
        self.routine(field)

    def test_phone(self, field='PHONE'):
        self.routine(field)

    def tearDown(self):
        self.header.select_option('Log out')


class TestAddressNegative(BasePage):

    def setUp(self):
        self.browser.driver.get(URL)
        start = SignInPage(self)
        self.perform = UserPage(self)
        start.login('USER')
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        button_disabled = self.perform.disabled_update_profile_button()
        assert not valid_entry and button_disabled

    def test_country(self, field='COUNTRY'):
        self.routine(field)

    def test_city(self, field='CITY'):
        self.routine(field)

    def test_street(self, field='STREET'):
        self.routine(field)

    def test_building(self, field='BUILDING'):
        self.routine(field)

    def test_apartment(self, field='APARTMENT'):
        self.routine(field)

    def test_zip_code(self, field='ZIP_CODE'):
        self.routine(field)

    def tearDown(self):
        self.header.select_option('Log out')