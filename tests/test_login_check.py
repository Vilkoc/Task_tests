from init import BasePage
from pages.sign_in_page import SignInPage
from config import URL


class TestLoginAll(BasePage):

    def setUp(self):
        self.browser.driver.get(URL)
        self.inquire = SignInPage(self)

    def routine(self, person):
        self.inquire.login(person)
        assert self.header.person_verify(person)

    def test_login_admin(self):
        self.routine('ADMIN')

    def test_login_user(self):
        self.routine('USER')

    def test_login_cowner(self):
        self.routine('COWNER')

    def tearDown(self):
        self.header.select_option('Log out')
        self.browser.driver.get(URL)

