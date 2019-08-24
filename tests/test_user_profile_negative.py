from init import SeleniumTestBase
from data_tests.user_data import user_data_rab_26 as entry


class TestFirstName(SeleniumTestBase):
    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_first_name(self, field='FIRST_NAME'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        button_disabled = self.user_profile_page.disabled_update_profile_button()
        assert not valid_entry
        assert button_disabled


class TestLastName(SeleniumTestBase):
    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_first_name(self, field='LAST_NAME'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        button_disabled = self.user_profile_page.disabled_update_profile_button()
        assert not valid_entry
        assert button_disabled


class TestCountry(SeleniumTestBase):
    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_country(self, field='COUNTRY'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        button_disabled = self.user_profile_page.disabled_update_profile_button()
        assert not valid_entry
        assert button_disabled


class TestPhone(SeleniumTestBase):
    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_phone(self, field='PHONE'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        button_disabled = self.user_profile_page.disabled_update_profile_button()
        assert not valid_entry
        assert button_disabled


class TestCity(SeleniumTestBase):
    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_city(self, field='CITY'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        button_disabled = self.user_profile_page.disabled_update_profile_button()
        assert not valid_entry
        assert button_disabled


class TestStreet(SeleniumTestBase):
    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_street(self, field='STREET'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        button_disabled = self.user_profile_page.disabled_update_profile_button()
        assert not valid_entry
        assert button_disabled


class TestBuilding(SeleniumTestBase):
    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_building(self, field='BUILDING'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        button_disabled = self.user_profile_page.disabled_update_profile_button()
        assert not valid_entry
        assert button_disabled


class TestApartment(SeleniumTestBase):
    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_apartment(self, field='APARTMENT'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        button_disabled = self.user_profile_page.disabled_update_profile_button()
        assert not valid_entry
        assert button_disabled


class TestZipCode(SeleniumTestBase):
    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_zip_code(self, field='ZIP_CODE'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        button_disabled = self.user_profile_page.disabled_update_profile_button()
        assert not valid_entry
        assert button_disabled
