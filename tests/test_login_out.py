from init import BasePage
import unittest
from pages.header import Header
from pages.sign_in_page import SignInPage


class TestTrial(BasePage):

    def test_login_logout(self, person='USER'):
        driver = self.driver
        start = Header(driver)
        signin = SignInPage(driver)


        start.transit('Log in')

        signin.login(person)

        start.transit('Profile')
        start.transit('Log out')

if __name__ == "__main__":
    unittest.main()
