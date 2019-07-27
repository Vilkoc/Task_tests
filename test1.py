from selenium import webdriver
from init import BasePage
import unittest
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from credentials import Credentials


class Test1(BasePage):

    def test_login_logout(self, person='USER'):
        driver = self.driver

        start = HomePage(driver)
        login = SignInPage(driver)
        start.click_icon()
        start.click_login()

        login.clear_box('email')
        login.send_keys('email', Credentials[person][0])
        login.clear_box('password')
        login.send_keys('password', Credentials[person][1])
        login.click_sign_in()
        login.click_logout()


if __name__ == "__main__":
    unittest.main()
