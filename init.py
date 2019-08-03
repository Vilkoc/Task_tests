from selenium import webdriver
from methods import Methods
from pages.header import Header
from driver_selection import WebdriverSelection
from utilities.db import prepare_db
from config import URL, TIMEOUT, WEBDRIVER


class BasePage():

    @classmethod
    def setUpClass(cls):
        prepare_db()
        cls.driver = WebdriverSelection().get_webdriver(WEBDRIVER)
        cls.driver.maximize_window()
        cls.driver.get(URL)
        cls.browser = Methods(cls.driver, TIMEOUT)
        cls.header = Header(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()