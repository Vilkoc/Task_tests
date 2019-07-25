from tests.locators.locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.login_icon_className = Locators.login_icon_className
        self.login_item_className = Locators.login_item_className
        self.email_textbox_id = Locators.email_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.singIn_button_css = Locators.singIn_button_css

    def go_to_loginPage(self):
        self.driver.find_element_by_class_name(self.login_icon_className).click()
        self.driver.find_element_by_class_name(self.login_item_className).click()

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_singIn_button(self):
        self.driver.find_element_by_css_selector(self.singIn_button_css).click()

    def login(self, email, password):
        self.go_to_loginPage()
        self.enter_email(email)
        self.enter_password(password)
        self.click_singIn_button()
