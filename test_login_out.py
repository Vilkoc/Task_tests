from init import BasePage
import unittest
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage


from credentials import Credentials


class Test1(BasePage):

    def test_login_logout(self, person='COWNER'):
        driver = self.driver

        start = HomePage(driver)
        login = SignInPage(driver)

        start.click_icon()
        start.click_dropdown('Log in')

        login.clear_boxes()
        login.enter_credentials(Credentials[person])
        login.click_sign_in()

        start.click_icon()
        start.click_dropdown('Profile')
        start.click_icon()
        start.click_dropdown('Log out')

if __name__ == "__main__":
    unittest.main()
