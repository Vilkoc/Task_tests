from init import BasePage
from pages.sign_in_page import SignInPage
from config import URL


class TestLoginAll(BasePage):

    def test_login_admin(self):
        person = 'ADMIN'
        inquire = SignInPage(self)
        inquire.login(person)
        assert self.header.person_verify(person)
        self.header.select_option('Log out')

    def test_login_user(self):
        person = 'USER'
        self.browser.driver.get(URL)
        inquire = SignInPage(self)
        inquire.login(person)
        assert self.header.person_verify(person)
        self.header.select_option('Log out')

    def test_login_cowner(self):
        person = 'COWNER'
        self.browser.driver.get(URL)
        inquire = SignInPage(self)
        inquire.login(person)
        assert self.header.person_verify(person)
        self.header.select_option('Log out')

