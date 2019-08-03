import time

from init import BasePage
import unittest
from pages.header import Header
from pages.auth_page import AuthPage

USER = 'user@gmail.com'
PASS = 'user'


class TestLogin(BasePage):

    def test_login_logout(self):
        header = Header(self.driver)
        page = AuthPage(self.driver)

        header.click_icon()
        header.click_log_in()

        page.enter_sign_in_email(USER)
        page.enter_sign_in_password(PASS)
        page.click_sign_in()

        assert header.is_logined()


if __name__ == "__main__":
    unittest.main()
