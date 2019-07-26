from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from tests import del_from_db
import unittest
import time


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://localhost:4200')
        cls.wait = WebDriverWait(cls.driver, 15)
        del_from_db.delete_from_vacancy_resume()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        # cls.driver.quit()
