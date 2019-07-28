
from selenium.webdriver.common.by import By


class Locators(object):

    ICON = (By.CSS_SELECTOR, "img[class='rounded-circle img-responsive z-depth-0']")
    LOGIN = (By.CSS_SELECTOR, "a[href='/users/auth']")
    SIGN_IN = (By.CSS_SELECTOR, "input[value='Sign In']")
    DROPDOWN = (By.CSS_SELECTOR, "a[class='dropdown-item']")
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")


class LocatorsUsers:
    pass

    # UPDATE_PROFILE = "input[value='Update Profile']"
   # DROPDOWN = "a[class='dropdown-item']"
    # NAVBAR = "a[class='navbar-brand']"
    # PHOTO_ID = "customFile"

    # UPDATE_PHOTO = "input[value='Update Photo']"
    #
    # USER_FIELDS = {
    #     'first_name_id': 'firstName',
    #     'last_name_id': 'lastName',
    #     'birthday_id': 'birthday',
    #     'email_id': 'email',
    #     'phone_id': 'phoneNumber',
    #     'country_id': 'country',
    #     'city_id': 'city',
    #     'street_id': 'street',
    #     'building_id': 'building',
    #     'apartment_id': 'apartment',
    #     'zipcode_id': 'zipCode'
    #     }




