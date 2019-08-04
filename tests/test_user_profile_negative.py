from init import BasePage
from pages.sign_in_page import SignInPage
from pages.user_profile_page import UserPage
from user_data import user_data_rab_26 as entry


class TestNegative(BasePage):

    def setUp(self):
        start = SignInPage(self)
        self.perform = UserPage(self)
        start.login('USER')
        self.header.select_option('Profile')

    def test_first_name(self, field='FIRST_NAME'):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        button_enabled = self.perform.check_submit_button()
        self.perform.clear_data_textbox(field)
        assert not valid_entry and not button_enabled

    def test_last_name(self, field='LAST_NAME'):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        button_enabled = self.perform.check_submit_button()
        self.perform.clear_data_textbox(field)
        assert not valid_entry and not button_enabled

    def test_email(self, field='EMAIL'):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        button_enabled = self.perform.check_submit_button()
        self.perform.clear_data_textbox(field)
        assert not valid_entry and not button_enabled

    def test_phone(self, field='PHONE'):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        button_enabled = self.perform.check_submit_button()
        self.perform.clear_data_textbox(field)
        assert not valid_entry and not button_enabled

    def test_country(self, field='COUNTRY'):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        button_enabled = self.perform.check_submit_button()
        self.perform.clear_data_textbox(field)
        assert not valid_entry and not button_enabled

    def test_country(self, field='COUNTRY'):
        valid_entry = self.perform.enter_data_textbox(field, entry[field])
        button_enabled = self.perform.check_submit_button()
        self.perform.clear_data_textbox(field)
        assert not valid_entry and not button_enabled

    def tearDown(self):
        self.header.select_option('Log out')