from methods import DriverWrapper
from pages.header import Header
from driver_selection import WebdriverSelection
from utilities.db import prepare_db
from config import URL, TIMEOUT, WEBDRIVER


class BasePage():

    @classmethod
    def setUpClass(cls):
#        prepare_db()
        cls.driver = WebdriverSelection().get_webdriver(WEBDRIVER)
        cls.driver.maximize_window()
        cls.driver.get(URL)
        cls.browser = DriverWrapper(cls.driver, TIMEOUT)
        cls.header = Header(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
