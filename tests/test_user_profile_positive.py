from init import SeleniumTestBase
from data_tests.user_data import user_data_rab_19 as entry


class TestFirstName(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_first_name(self, field='FIRST_NAME'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read
        assert valid_entry


class TestLastName(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_last_name(self, field='LAST_NAME'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read
        assert valid_entry


class TestEmail(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_email(self, field='EMAIL'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read
        assert valid_entry


class TestPhone(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_phone(self, field='PHONE'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read
        assert valid_entry


class TestCountry(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_country(self, field='COUNTRY'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read
        assert valid_entry

class TestCity(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_city(self, field='CITY'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read
        assert valid_entry


class TestStreet(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_street(self, field='STREET'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read
        assert valid_entry


class TestBuilding(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_building(self, field='BUILDING'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read
        assert valid_entry


class TestApartment(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_apartment(self, field='APARTMENT'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read
        assert valid_entry


class TestZipCode(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('USER')
        self.header.select_option('Profile')

    def test_zip_code(self, field='ZIP_CODE'):
        valid_entry = self.user_profile_page.enter_data_textbox(field, entry[field])
        self.user_profile_page.click_update_profile()
        read = self.user_profile_page.read_data_textbox(field)
        assert entry[field] == read
        assert valid_entry
