from selenium import webdriver
import unittest
from methods import Methods
from pages.header import Header
from utilities.db import prepare_db
from config import TIMEOUT
from del_from_db import delete_from_vacancy_resume
import time


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        prepare_db()
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://localhost:4200')
        cls.browser = Methods(cls.driver, TIMEOUT)
        cls.header = Header(cls.driver)
        # delete_from_vacancy_resume()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()
