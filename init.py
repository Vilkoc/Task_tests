from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import del_from_db
import unittest


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
        cls.driver.quit()
