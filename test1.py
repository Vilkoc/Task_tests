from selenium import webdriver
from init import BasePage
import unittest
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from credentials import Credentials
import time


class Test1(BasePage):


    def test_login_logout(self, person='USER'):
        driver = self.driver

        start = HomePage(driver)
        login = SignInPage(driver)
        start.click_icon()
        time.sleep(1)
        start.click_login()
        time.sleep(1)

        login.clear_box('email')
        login.send_keys('email', Credentials[person][0])
        login.clear_box('password')
        login.send_keys('password', Credentials[person][1])
        login.click_sign_in()
        time.sleep(2)
        login.click_logout()
        time.sleep(4)



if __name__ == "__main__":
    unittest.main()
