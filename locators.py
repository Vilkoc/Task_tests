from selenium.webdriver.common.by import By


class LocatorsHeader():
    ICON = (By.CSS_SELECTOR, "img[class='rounded-circle img-responsive z-depth-0']")
    DROPDOWN = (By.CSS_SELECTOR, "a[class='dropdown-item']")
    CHECK_DROPDOWN = (By.CSS_SELECTOR, "a[data-toggle='dropdown']")
    NAVBAR = (By.CSS_SELECTOR, "a[class='navbar-brand']")

class LocatorsSignIn():
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SIGN_IN = (By.CSS_SELECTOR, "input[value='Sign In']")
    SIGNUP = (By.ID, "login1")
    PASSWORD_SIGNUP = (By.ID, "password1")
    PASSWORD_VERIFY = (By.ID, "matchingPassword")
    REGISTER_BTN = (By.CSS_SELECTOR, "input[value='Register']")

class LocatorsCompaniesPage(object):
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
    COMPANY_UPDATE_BUTTON_VALSOFT = (By.CSS_SELECTOR, "a[href='/updateCompany/ValSoft']")
    TABLE_BODY = (By.CSS_SELECTOR, "table>tbody")
    DELETE_COMPANY_BUTTON = (By.CSS_SELECTOR, "a>i[class='fa fa-trash']")
    COMPANY_UPDATE_BUTTON = (By.CSS_SELECTOR, "a>i[class='fa fa-edit']")


class LocatorsCreateVacancyPage(object):
    CREATE_VACANCY_BUTTON = (By.CSS_SELECTOR, "a[href='/createVacancy/1']" )
    VACANCY_DESCRIPTION_TEXTBOX =(By.ID, "description")
    VACANCY_POSITION_TEXTBOX = (By.ID, "position")
    VACANCY_EMPLOYMENT_DROPBOX = (By.CSS_SELECTOR, "select>option[value='HOURLY']")
    VACANCY_SALARY_TEXTBOX = (By.ID, "salary")
    VACANCY_CURRRENCY_DROPBOX = (By.CSS_SELECTOR, "select>option[value='USD']")
    ADD_REQUIREMENT_BUTTON =(By.CSS_SELECTOR, "button[class='btn btn-success']")
    VACANCY_REQUIREMENT_TEXTBOX = (By.ID, "description")
    VAC_REQUIREMENT_TEXTBOX = (By.CSS_SELECTOR, "input[id = 'description'][placeholder = 'Input requirement']")
    VACANCY_CREATE_BUTTON =(By.CSS_SELECTOR, "button[class='btn btn-primary'][type='submit']")

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
