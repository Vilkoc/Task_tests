from selenium.webdriver.common.by import By


class LocatorsHeader():
    ICON = (By.CSS_SELECTOR, "img[class='rounded-circle img-responsive z-depth-0']")
    DROPDOWN = (By.CSS_SELECTOR, "a[class='dropdown-item']")
    CHECK_DROPDOWN = (By.CSS_SELECTOR, "a[data-toggle='dropdown']")
    NAVBAR = (By.CSS_SELECTOR, "a[class='navbar-brand']")
    LOG_IN = (By.CSS_SELECTOR, "a[class='dropdown-item']"), "Log in"
    LOG_OUT = (By.CSS_SELECTOR, "a[class^='dropdown-item']"), "Log out"
    LINKS = (By.CSS_SELECTOR, 'a[class="navbar-brand"]')
    RABOTY_NET = (By.LINK_TEXT, "RabotyNet")


class LocatorsSignIn():
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SIGN_IN = (By.CSS_SELECTOR, "input[value='Sign In']")
    SIGNUP = (By.ID, "login1")
    PASSWORD_SIGNUP = (By.ID, "password1")
    PASSWORD_VERIFY = (By.ID, "matchingPassword")
    REGISTER_BTN = (By.CSS_SELECTOR, "input[value='Register']")
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


class LocatorsCompaniesPage(object):
    SHOW_CLAIMS_BUTTON = (By.CSS_SELECTOR, 'a[title = "Show"]')
    DESCRIPTION = (By.CSS_SELECTOR, 'table[class="table table-stripped"]>tbody>tr>td')


class LocatorsCreateCompanyPage(object):
    CREATE_COMPANY_TAB = (By.CSS_SELECTOR, "a[class='navbar-brand'][href='/createCompany']")
    COMPANY_NAME_TEXBOX = (By.ID, "name")
    COMPANY_EDRPOU_TEXBOX = (By.ID, "edrpou")
    COMPANY_DESCRIPTION_TEXTBOX = (By.ID, "description")
    COMPANY_WEBSITE_TEXTBOX = (By.ID, "website")
    COMPANY_EMAIL_TEXTBOX = (By.ID, "email")
    COMPANY_PHONE_NUMBER_TEXTBOX = (By.ID, "phoneNumber")
    COMPANY_COUNTRY_TEXTBOX = (By.ID, "country")
    COMPANY_CITY_TEXTBOX = (By.ID, "city")
    COMPANY_STREET_TEXTBOX = (By.ID, "street")
    COMPANY_BUILDING_TEXTBOX = (By.ID, "building")
    COMPANY_APARTMENT_TEXTBOX = (By.ID, "apartment")
    COMPANY_ZIPCODE_TEXTBOX = (By.ID, "zipCode")
    COMPANY_CREATE_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-primary']")
    ATTRIBUTE_OF_COMPANIES_VACANCIES_TEXTBOXES = "ng-reflect-model"

    COMPANY_FIELDS = ["name", "edrpou", "description", "website", "email", "phoneNumber", "country", "city", "street",
                      "building", "apartment", "zipCode"]
    MY_COMPANIES = (By.CSS_SELECTOR, "a[href='/companies/my']")


class LocatorsUpdateCompanyPage(LocatorsCreateCompanyPage):
    INPUT_FIELD = (By.CSS_SELECTOR, "input[id = 'customFile']")
    UPDATE_PHOTO_BUTTON = (By.CSS_SELECTOR, "input[class='btn btn-primary']")
    UPDATE_COMPANY_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    GO_BACK_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-danger']")


class LocatorsMyCompaniesPage(object):
    MY_COMPANIES = (By.CSS_SELECTOR, "a[href='/companies/my']")
    CREATE_COMPANY_BUTTON = (By.CSS_SELECTOR, "a[href='/createCompany']")
    COMPANY_DETAIL_BUTTON_SOFTSERVE = (By.CSS_SELECTOR, "a[href ='/viewCompany/1']")
    TABLE_BODY = (By.CSS_SELECTOR, "table>tbody")
    DELETE_COMPANY_BUTTON = (By.CSS_SELECTOR, "a>i[class='fa fa-trash']")
    COMPANY_UPDATE_BUTTON = (By.CSS_SELECTOR, "a>i[class='fa fa-edit']")


class LocatorsViewCompany(object):
    CREATE_VACANCY_BUTTON = (By.CSS_SELECTOR, "a[href='/createVacancy/1']")
    VACANCY_DETAILS_BUTTON = (By.PARTIAL_LINK_TEXT, "View details")
    SIMPLE_VACANCY_DIV = (By.CSS_SELECTOR, "div.simpleVacancy")
    CLAIM_BUTTON = (By.CSS_SELECTOR, 'button[class = "btn btn-warning"]')
    TITLE = (By.CSS_SELECTOR, 'select[id="title"]>option')
    DESCRIPTION_FIELD = (By.ID, 'description')
    SEND_CLAIM_BUTTON = (By.CSS_SELECTOR, 'input[value="Claim"]')


class LocatorsCreateVacancyPage(object):
    VACANCY_DESCRIPTION_TEXTBOX = (By.ID, "description")
    VACANCY_POSITION_TEXTBOX = (By.ID, "position")
    VACANCY_EMPLOYMENT_DROPBOX = (By.CSS_SELECTOR, "select>option[value='HOURLY']")
    VACANCY_SALARY_TEXTBOX = (By.ID, "salary")
    VACANCY_CURRRENCY_DROPBOX = (By.CSS_SELECTOR, "select>option[value='USD']")
    ADD_REQUIREMENT_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    VAC_REQUIREMENT_TEXTBOX = (By.CSS_SELECTOR, "input[id = 'description'][placeholder = 'Input requirement']")
    VACANCY_CREATE_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-primary'][type='submit']")

    VACANCY_FIELDS = ["description", "position", "salary"]


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


class LocatorsForgotPassword:
    EMAIL = (By.ID, 'username')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[value="Submit"]')


class LocatorsConfirmPassword:
    NEW_PASSWORD = (By.ID, 'newPassword')
    CONFIRMATION_PASSWORD = (By.ID, 'confirmPassword')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'input[value="Register"]')


class LocatorsPreviewResume(object):
    BUTTONS = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')
    MESSAGE = (By.CSS_SELECTOR, 'div[class="wrap"]>p')
    PREVIEW_PDF_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')
    RESUME = (By.CSS_SELECTOR, "div[class='form-group']>iframe")


class LocatorsYourResume(object):
    SHOW_ALL_INFO_BUTTON = (By.CSS_SELECTOR, 'a[href="/update/2"]')


class LocatorsVacancies(object):
    VIEW_DETAILS_BUTTON = (By.CSS_SELECTOR, 'a[href="/viewVacancy/34"]')
    POP_UP_WINDOW_SIGN_UP_TEXT = (By.CSS_SELECTOR, 'div.wrap > p')
    POP_UP_WINDOW_SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'div.wrap > button')

    POP_UP_WINDOW_FORGOT_PASSWORD_TEXT = (By.CSS_SELECTOR, 'div.wrap > p')
    POP_UP_WINDOW_FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'div.wrap > button')


class LocatorsViewVacancy(object):
    SEND_RESUME_BUTTON = (By.CSS_SELECTOR, 'a[class="btn btn-success"]')
    SHOW_COMPANY_BUTTON = (By.CSS_SELECTOR, 'a[href="/viewCompany/1"]')
    TEXT = (By.CSS_SELECTOR, "div[class='simpleVacancy']>td")


class LocatorsEditResume(object):
    POSITION_FIELD = (By.ID, 'position')
    PREVIEW_PDF_BUTTON = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')
    GET_TEXT_FROM_FIELD = 'ng-reflect-model'
