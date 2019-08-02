from selenium.webdriver.common.by import By


class LocatorsHeader():
    ICON = (By.CSS_SELECTOR, "img[class='rounded-circle img-responsive z-depth-0']")
    DROPDOWN = (By.CSS_SELECTOR, "a[class='dropdown-item']")
    CHECK_DROPDOWN = (By.CSS_SELECTOR, "a[data-toggle='dropdown']")
    NAVBAR = (By.CSS_SELECTOR, "a[class='navbar-brand']")
    RABOTY_NET = (By.LINK_TEXT, "RabotyNet")


class LocatorsSignIn():
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SIGN_IN = (By.CSS_SELECTOR, "input[value='Sign In']")
    SIGNUP = (By.ID, "login1")
    PASSWORD_SIGNUP = (By.ID, "password1")
    PASSWORD_VERIFY = (By.ID, "matchingPassword")
    REGISTER_BTN = (By.CSS_SELECTOR, "input[value='Register']")


class LocatorsPreviewResume(object):
    BUTTONS = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')
    MESSAGE = (By.CSS_SELECTOR, 'div[class="wrap"]>p')
    PREVIEW_PDF_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')


class LocatorsYourResume(object):
    SHOW_ALL_INFO_BUTTON = (By.CSS_SELECTOR, 'a[href="/update/2"]')


class LocatorsVacancies(object):
    VIEW_DETAILS_BUTTON = (By.CSS_SELECTOR, 'a[href="/viewVacancy/34"]')


class LocatorsViewVacancy(object):
    SEND_RESUME_BUTTON = (By.CSS_SELECTOR, 'a[class="btn btn-success"]')
    SHOW_COMPANY_BUTTON = (By.CSS_SELECTOR, 'a[href="/viewCompany/34"]')
    TEXT = (By.CSS_SELECTOR, "div[class='simpleVacancy']>td")
