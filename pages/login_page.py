LOGIN_ICON_CLASS_NAME = 'dropdown'
LOGIN_ITEM_CLASS_NAME = 'dropdown-item'
EMAIL_TEXTBOX_ID = 'username'
PASSWORD_TEXTBOX_ID = 'password'
SIGN_IN_BUTTON_CSS_SELECTOR = 'input[value="Sign In"]'


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.login_icon_className = LOGIN_ICON_CLASS_NAME
        self.login_item_className = LOGIN_ITEM_CLASS_NAME
        self.email_textbox_id = EMAIL_TEXTBOX_ID
        self.password_textbox_id = PASSWORD_TEXTBOX_ID
        self.singIn_button_css = SIGN_IN_BUTTON_CSS_SELECTOR

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
