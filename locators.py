from selenium.webdriver.common.by import By


class LocatorsHeader():
    ICON = (By.CSS_SELECTOR, "img[class='rounded-circle img-responsive z-depth-0']")
    DROPDOWN = (By.CSS_SELECTOR, "a[class='dropdown-item']")
    CHECK_DROPDOWN = (By.CSS_SELECTOR, "a[data-toggle='dropdown']")
    NAVBAR = (By.CSS_SELECTOR, "a[class='navbar-brand']")
    MOVE_TO_COMPANIES = (By.CSS_SELECTOR, 'a[href="/companies"]')


class LocatorsSignIn():
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SIGN_IN = (By.CSS_SELECTOR, "input[value='Sign In']")

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
    FILTER_CITY = (By.CSS_SELECTOR, 'tbody>tr')


class LocatorsCompaniesPage(object):
    STATUS_APPROVED = (By.CSS_SELECTOR, 'i[class="fa fa-thumbs-up"]')
    STATUS_NOT_APPROVED = (By.CSS_SELECTOR, 'i[class="fa fa-times"]')
    STATUS_BLOCKED = (By.CSS_SELECTOR, 'i[class="fa fa-lock"]')
    STATUS_WARNING = (By.CSS_SELECTOR, 'i[class="fa fa-warning"]')
    BLOCK_1_CO = (By.CSS_SELECTOR, 'a[title="Block"]')
    UNBLOCK_2_CO = (By.CSS_SELECTOR, 'a[title="Unblock"]')
    DETAILS_ABOUT_CO = (By.CSS_SELECTOR, 'a[href="/viewCompany/1"]')
    APPROVE_CO = (By.CSS_SELECTOR, 'a[title="Approve"]')
    OPEN_CLAIM_BTN = (By.CSS_SELECTOR, 'a[title="Show"]')
    REJECT_CLAIM_BTN = (By.CSS_SELECTOR, 'button[title"Reject claim"]')
    CLOSE_CLAIM_BTN = (By.CSS_SELECTOR, 'a[title="Hide"]')
    POPUP = (By.CSS_SELECTOR, 'div.wrap')
    TABLE_BODY = (By.CSS_SELECTOR, "table > tbody")


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


class LocatorsCompaniesDetailsPage:
    CREATE_CLAIM_BTN = (By.CSS_SELECTOR, 'button[class="btn btn-warning"]')
    CANCEL_CLAIM_BTN = (By.CSS_SELECTOR, 'input[value="Cancel"]')
    SEND_CLAIM_BTN = (By.CSS_SELECTOR, 'input[class="btn btn-danger"]')
    SELECT_TITLE = (By.CSS_SELECTOR, 'option[value="None"')
    CLAIM_DESCRIPTION = (By.CSS_SELECTOR, '#description')
    DESCRIPTION_OF_CLAIM = 'Description'

