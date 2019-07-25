from pages.home_page import HomePage
from pages.sign_in_page import SignInPage

from init import BasePage
import unittest


class TestLoginPage(BasePage):

    def test_login(self):
        start = HomePage(self.driver)
        login = SignInPage(self.driver)
        start.click_icon()
        start.click_login()
        login.enter_email("user@gmail.com")
        login.enter_password("user")
        login.click_sign_in()


if __name__ == '__main__':
    unittest.main()
