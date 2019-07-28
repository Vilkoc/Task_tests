from selenium import webdriver
from init import BasePage
import unittest
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from credentials import Credentials
from selenium.webdriver.common.by import By


class Test1(BasePage):

    def test_login_logout(self, person='USER'):
        driver = self.driver

        start = HomePage(driver)
        login = SignInPage(driver)
        start.click_icon()
        start.click_login()
        login.clear_boxes()
        login.enter_credentials(Credentials[person])
        login.click_sign_in()
        login.click_logout()


if __name__ == "__main__":
    unittest.main()
