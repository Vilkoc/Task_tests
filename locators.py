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


class LocatorsCompaniesPage(object):
    SHOW_CLAIMS_BUTTON = (By.CSS_SELECTOR, 'a[title = "Show"]')
    DESCRIPTION = (By.CSS_SELECTOR, 'table[class="table table-stripped"]>tbody>tr>td')

    STATUS_OF_CO = (By.CSS_SELECTOR, 'i[title]')

    BLOCK_1_CO = (By.CSS_SELECTOR, 'a[title="Block"]')

    UNBLOCK_2_CO = (By.CSS_SELECTOR, 'a[title="Unblock"]')

    DETAILS_ABOUT_CO = (By.CSS_SELECTOR, 'a[href="/viewCompany/1"]')

    APPROVE_CO = (By.CSS_SELECTOR, 'a[title="Approve"]')
    ###########################################
    button_next_css = (By.CSS_SELECTOR, 'button')

    PREVIEWS_PAGE_BTN = (By.CSS_SELECTOR, 'body > div > div > section > div > div > button:nth-child(4)')

    OPEN_CLAIM_BTN = (By.CSS_SELECTOR, 'a[title="Show"]')

    REJECT_CLAIM_BTN = (By.CSS_SELECTOR, 'button[title"Reject claim"]')

    CLOSE_CLAIM_BTN = (By.CSS_SELECTOR, 'a[title="Hide"]')

    name_of_1company_css = (By.CSS_SELECTOR, 'body > div > div > section > div > div > table >\
     tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')

    POPUP = (By.CSS_SELECTOR, 'div.wrap')


class LocatorsUserPage():
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


class LocatorsPreviewResume(object):
    BUTTONS = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')
    MESSAGE = (By.CSS_SELECTOR, 'div[class="wrap"]>p')
    PREVIEW_PDF_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')
    RESUME = (By.CSS_SELECTOR, "div[class='form-group']>iframe")


class LocatorsYourResume(object):
    SHOW_ALL_INFO_BUTTON = (By.CSS_SELECTOR, 'a[href="/update/2"]')


class LocatorsVacancies(object):
    VIEW_DETAILS_BUTTON = (By.CSS_SELECTOR, 'a[href="/viewVacancy/34"]')


class LocatorsViewVacancy(object):
    SEND_RESUME_BUTTON = (By.CSS_SELECTOR, 'a[class="btn btn-success"]')
    SHOW_COMPANY_BUTTON = (By.CSS_SELECTOR, 'a[href="/viewCompany/1"]')
    TEXT = (By.CSS_SELECTOR, "div[class='simpleVacancy']>td")


class LocatorsEditResume(object):
    POSITION_FIELD = (By.ID, 'position')
    PREVIEW_PDF_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')
    GET_TEXT_FROM_FIELD = 'ng-reflect-model'


class LocatorsViewCompany(object):
    CLAIM_BUTTON = (By.CSS_SELECTOR, 'button[class = "btn btn-warning"]')
    TITLE = (By.CSS_SELECTOR, 'select[id="title"]>option')
    DESCRIPTION_FIELD = (By.ID, 'description')
    SEND_CLAIM_BUTTON = (By.CSS_SELECTOR, 'input[value="Claim"]')
