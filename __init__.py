from selenium import webdriver
from tests import cleanDB
import unittest


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://localhost:4200/vacancies')
        # cleanDB.prepare_database()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
