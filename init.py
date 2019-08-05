from methods import DriverWrapper
from pages.header import Header
from driver_selection import WebdriverSelection
from utilities.db import prepare_db
from config import URL, TIMEOUT, WEBDRIVER


class BasePage():

    @classmethod
    def setUpClass(cls):
        # prepare_db()
        driver = WebdriverSelection().get_webdriver(WEBDRIVER)
        driver.maximize_window()
        driver.get(URL)
        cls.browser = DriverWrapper(driver, TIMEOUT)
        cls.header = Header(cls)


    @classmethod
    def tearDownClass(cls):
        cls.browser.driver.quit()
