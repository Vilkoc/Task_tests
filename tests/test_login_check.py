import unittest

from init import BasePage
from pages.sign_in_page import SignInPage


class TestLoginAll(BasePage):
    @unittest.skip('skip due to: "https://ssu-jira.softserveinc.com/browse/RAB-86"')

    def test_login_all(self):
        person = 'ADMIN'
        inquire = SignInPage(self)

        inquire.login(person)

        assert self.header.person_verify(person)

        self.header.select_option('Log out')

