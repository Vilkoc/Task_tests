from init import BasePage
import unittest
from pages.header import Header
from pages.sign_in_page import SignInPage
import time


class TestTrial(BasePage):

    def test_login_logout(self, person='COWNER'):
        driver = self.driver
        start = Header(driver)
        signin = SignInPage(driver)

        start.transit('Log in')

        signin.login(person)
        time.sleep(2)
        start.transit('Profile')
        time.sleep(2)
        start.transit('Log out')


if __name__ == "__main__":
    unittest.main()
