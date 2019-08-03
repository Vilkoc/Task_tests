from selenium.webdriver.common.by import By


class LocatorsHeader(object):
    ICON = (By.CSS_SELECTOR, "img[class='rounded-circle img-responsive z-depth-0']")
    DROPDOWN = (By.CSS_SELECTOR, "a[class='dropdown-item']")
    LOG_IN = (By.CSS_SELECTOR, "a[class='dropdown-item']"), "Log in"
    LOG_OUT = (By.CSS_SELECTOR, "a[class^='dropdown-item']"), "Log out"


class LocatorsSignIn(object):
    EMAIL_SIGN_IN = (By.ID, "username")
    PASSWORD_SIGN_IN = (By.ID, "password")
    BUTTON_SIGN_IN = (By.CSS_SELECTOR, "input[value='Sign In']")

    TAB_SIGN_UP = (By.CLASS_NAME, 'tablinks'), 'Sign Up'

    EMAIL_SIGN_UP = (By.ID, "login1")
    PASSWORD_SIGN_UP = (By.ID, "password1")
    PASSWORD_MATCHING_SIGN_UP = (By.ID, "matchingPassword")
    BUTTON_SIGN_UP = (By.CSS_SELECTOR, "input[value='Register']")
    NAVBAR = (By.CSS_SELECTOR, "a[class='navbar-brand']")

    FORGOT_PASSWORD = (By.CSS_SELECTOR, 'a[href="/forgotPassword"]')
    POP_UP_FORGOT_PASSWORD = (By.CSS_SELECTOR, 'div.wrap')
    POP_UP_FORGOT_PASSWORD_TEXT = (By.TAG_NAME, 'p')
    POP_UP_FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'div.wrap > button')
    POP_UP_FORGOT_PASSWORD_TEXT_CHECK = 'Password restored successfully! Please sign in.'


class LocatorsVacanvies:
    POP_UP_WINDOW_SIGN_UP_TEXT = (By.CSS_SELECTOR, 'div.wrap > p')
    POP_UP_WINDOW_SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'div.wrap > button')

    POP_UP_WINDOW_FORGOT_PASSWORD_TEXT = (By.CSS_SELECTOR, 'div.wrap > p')
    POP_UP_WINDOW_FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'div.wrap > button')

class LocatorsForgotPassword:
    EMAIL = (By.ID, 'username')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[value="Submit"]')


class LocatorsConfirmPassword:
    NEW_PASSWORD = (By.ID, 'newPassword')
    CONFIRMATION_PASSWORD = (By.ID, 'confirmPassword')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'input[value="Register"]')
