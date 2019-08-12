from pages.auth_page import AuthPage
import allure


def login(sign_in_page, user, password):
    sign_in_page.enter_sign_in_email(user)
    sign_in_page.enter_sign_in_password(password)
    sign_in_page.click_sign_in()

def get_screenshot(driver, name):
    allure.attach(driver.get_screenshot_as_png, name=name, attachment_type=allure.attachment_type.PNG)