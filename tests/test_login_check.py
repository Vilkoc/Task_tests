from init import BasePage
from pages.sign_in_page import SignInPage
from credentials import Credentials


class TestLoginAll(BasePage):

    def test_login_all(self):
        for person in Credentials.keys():
            inquire = SignInPage(self)

            inquire.login(person)
            assert self.header.person_verify(person)
            self.header.select_option('Log out')

