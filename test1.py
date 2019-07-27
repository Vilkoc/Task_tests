from selenium import webdriver
from init import BasePage
import unittest
from pages.pages import HomePage
from credentials import Credentials
import time


class Test1(BasePage):

    def test_login_valid(self):
        driver = self.driver

        start = HomePage(driver)
        start.click_icon()
        time.sleep(1)
        start.click_login()
        time.sleep(1)
        start.clear_box('email')
        start.send_keys('email', Credentials.user_login)
        start.clear_box('password')
        start.send_keys('password', Credentials.user_password)
        start.click_sign_in()
        time.sleep(2)



if __name__ == "__main__":
    unittest.main()
