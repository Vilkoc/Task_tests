from selenium.webdriver.common.by import By


class LocatorsHeader(object):
    ICON = (By.CSS_SELECTOR, "img[class='rounded-circle img-responsive z-depth-0']")
    DROPDOWN = (By.CSS_SELECTOR, "a[class='dropdown-item']")


class LocatorsSignIn(object):
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SIGN_IN = (By.CSS_SELECTOR, "input[value='Sign In']")
    SIGNUP = (By.ID, "login1")
    PASSWORD_SIGNUP = (By.ID, "password1")
    PASSWORD_VERIFY = (By.ID, "matchingPassword")
    REGISTER_BTN = (By.CSS_SELECTOR, "input[value='Register']")
    NAVBAR = (By.CSS_SELECTOR, "a[class='navbar-brand']")


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


class MyCompaniesPage(object):
    CREATE_COMPANY_BUTTON = (By.CSS_SELECTOR, "a[href='/createCompany']")