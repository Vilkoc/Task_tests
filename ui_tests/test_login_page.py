from tests.pages.login_page import LoginPage
from tests import BasePage
import unittest


class TestLoginPage(BasePage):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login('user@gmail.com', 'user')


if __name__ == '__main__':
    unittest.main()
