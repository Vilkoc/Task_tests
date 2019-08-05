from init import BasePage
from pages.sign_in_page import SignInPage
from pages.user_profile_page import UserPage
from data_tests.user_data import user_data_rab_19 as entry
from config import URL


class TestNamePositive(BasePage):

    def setUp(self):
        self.browser.driver.get(URL)
        start = SignInPage(self)
        self.perform = UserPage(self)
        start.login('USER')
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        self.perform.click_update_profile()
        read = self.perform.read_data_textbox(field)
        assert entry[field] == read and valid_entry

    def test_first_name(self, field='FIRST_NAME'):
        self.routine(field)

    def test_last_name(self, field='LAST_NAME'):
        self.routine(field)

    def tearDown(self):
        self.header.select_option('Log out')


class TestContactsPositive(BasePage):

    def setUp(self):
        self.browser.driver.get(URL)
        start = SignInPage(self)
        self.perform = UserPage(self)
        start.login('USER')
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        self.perform.click_update_profile()
        read = self.perform.read_data_textbox(field)
        assert entry[field] == read and valid_entry

    def test_email(self, field='EMAIL'):
        self.routine(field)

    def test_phone(self, field='PHONE'):
        self.routine(field)

    def tearDown(self):
        self.header.select_option('Log out')


class TestAddressPositive(BasePage):

    def setUp(self):
        self.browser.driver.get(URL)
        start = SignInPage(self)
        self.perform = UserPage(self)
        start.login('USER')
        self.header.select_option('Profile')

    def routine(self, field):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        self.perform.click_update_profile()
        read = self.perform.read_data_textbox(field)
        assert entry[field] == read and valid_entry

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
