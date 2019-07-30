from selenium import webdriver
import unittest
from methods import Methods
from pages.header import Header
from utilities.db import prepare_db
from config import TIMEOUT


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        prepare_db()
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://localhost:4200')
        cls.browser = Methods(cls.driver, TIMEOUT)
        cls.header = Header(cls.driver)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
