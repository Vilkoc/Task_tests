from selenium.webdriver.common.by import By


class LocatorsHeader(object):
    ICON = (By.CSS_SELECTOR, "img[class='rounded-circle img-responsive z-depth-0']")
    DROPDOWN = (By.CSS_SELECTOR, "a[class='dropdown-item']")
    CHECK_DROPDOWN = (By.CSS_SELECTOR, "a[data-toggle='dropdown']")
    NAVBAR = (By.CSS_SELECTOR, "a[class='navbar-brand']")


class LocatorsSignIn(object):
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SIGN_IN = (By.CSS_SELECTOR, "input[value='Sign In']")
    SIGNUP = (By.ID, "login1")
    PASSWORD_SIGNUP = (By.ID, "password1")
    PASSWORD_VERIFY = (By.ID, "matchingPassword")
    REGISTER_BTN = (By.CSS_SELECTOR, "input[value='Register']")


class LocatorsVacancies(object):
    DETAILS = (By.CSS_SELECTOR, 'a[href="/viewVacancy/34"]')
    PAGINATION_NEXT = (By.CSS_SELECTOR, 'button[class="btn btn-info"]')
    PAGINATION_PREVIOUS = (By.CSS_SELECTOR, 'button[class="btn btn-info"]')
    VACANCY_INFO = (By.CSS_SELECTOR, 'div[class="card"]>h2')
    NEXT_TEST = (By.CSS_SELECTOR, 'div[class="card"]>h2')
    PREVIOUS_TEST = (By.CSS_SELECTOR, 'div[class="card"]>h2')


class LocatorsHotVacancies(object):
    HOT_DETAILS = (By.CSS_SELECTOR, 'a[href="/viewVacancy/34"]')
    HOT_PAGINATION_NEXT = (By.CSS_SELECTOR, 'button[class="btn btn-info"]')
    HOT_PAGINATION_PREVIOUS = (By.CSS_SELECTOR, 'button[class="btn btn-info"]')
    HOT_VACANCY_INFO = (By.CSS_SELECTOR, 'div[class="card"]>h2')
    HOT_NEXT_TEST = (By.CSS_SELECTOR, 'div[class="card"]>h2')
    HOT_PREVIOUS_TEST = (By.CSS_SELECTOR, 'div[class="card"]>h2')
    HOT_VACANCY_PAGE = (By.CSS_SELECTOR, 'a[href="/hotVacancies"]')


class LocatorsSearch(object):
    SEARCH = (By.CSS_SELECTOR, 'button[class="btn btn-outline-success my-2 my-sm-0"]')
    CRITERIA = (By.CSS_SELECTOR, 'option[value="city"]')
    KEY_WORD = (By.NAME, 'searchText')
    SEARCH_START = (By.ID, 'startButton')



class LocatorsUserPage:
    UPDATE_PROFILE = (By.CSS_SELECTOR, "input[value='Update Profile']")
    user_fields = {
        'FIRST_NAME': (By.ID, 'firstName'),
        'LAST_NAME': (By.ID, 'lastName'),
        'BIRTHDAY': (By.ID, 'birthday'),
        'EMAIL': (By.ID, 'email'),
        'PHONE': (By.ID, 'phoneNumber'),
        'COUNTRY': (By.ID, 'country'),
        'CITY': (By.ID, 'city'),
        'STREET': (By.ID, 'street'),
        'BUILDING': (By.ID, 'building'),
        'APARTMENT': (By.ID, 'apartment'),
        'ZIP_CODE': (By.ID, 'zipCode')
    }
