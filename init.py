from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import del_from_db
import unittest

TIMEOUT = 10

class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://localhost:4200')
        del_from_db.delete_from_vacancy_resume()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
