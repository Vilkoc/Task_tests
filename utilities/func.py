from pages.auth_page import AuthPage

def login(browser, user, password):
    sign_in_page = AuthPage(browser)
    sign_in_page.enter_sign_in_email(user)
    sign_in_page.enter_sign_in_password(password)
    sign_in_page.click_sign_in()