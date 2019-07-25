from selenium.webdriver.common.by import By
from locators.locators import Locators
from pages.home_page import HomePage

class SignInPage(HomePage):
    """Sign in page, it also checks if sign in is complete"""
    def __init__(self, driver):
        self.driver = driver
        self.email_field = Locators.email_sign_in_id
        self.password_field = Locators.password_link_id
        self.sign_in_button = Locators.sign_in_css_selector
        #self.nav_bar = Locators.navbar_css_selector

    def enter_email(self, user_email):
        self.driver.find_element(By.ID, self.email_field).clear()
        self.driver.find_element(By.ID, self.email_field).send_keys(user_email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field).clear()
        self.driver.find_element(By.ID, self.password_field).send_keys(password)

    def click_sign_in(self):
        elem_1 = self.driver.find_element(By.CSS_SELECTOR, self.sign_in_button)
        elem_1.click()
        # elem_2 = self.driver.find_elements(By.CSS_SELECTOR, self.nav_bar)
        # while len(elem_2) <= 2: #Checking if SignIn finished
        #     elem_2 = self.driver.find_elements(By.CSS_SELECTOR, self.nav_bar)
