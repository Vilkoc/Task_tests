from methods import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT, WEBDRIVER
from pages.header import Header
from utilities.db import prepare_db


class BasePage():

    @classmethod
    def setUpClass(cls):
        prepare_db()
        driver = WebdriverSelection().get_webdriver(WEBDRIVER)
        driver.maximize_window()
        driver.get(URL)
        cls.browser = DriverWrapper(driver, TIMEOUT)
        cls.header = Header(cls)

    @classmethod
    def tearDownClass(cls):
        pass
        # cls.browser.driver.quit()
