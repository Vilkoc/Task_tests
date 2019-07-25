from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import Locators

class HomePage:
    """Home page description, is parent for ____Page"""
    def __init__(self, driver):
        self.driver = driver
        self.icon_link = Locators.icon_css_selector
        self.login_button = Locators.login_btn_css_selector

    def click_icon(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.icon_link)))
        elem = self.driver.find_element(By.CSS_SELECTOR, self.icon_link)
        elem.click()

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()
