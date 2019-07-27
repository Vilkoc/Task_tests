class Locators:

    ICON = "img[class='rounded-circle img-responsive z-depth-0']"
    LOGIN = "a[href='/users/auth']"
    ID_LOC = {
        'email': "username",
        'password': "password"
    }
    SIGN_IN = "input[value='Sign In']"
    DROPDOWN = "a[class='dropdown-item']"


class LocatorsUsers:

    UPDATE_PROFILE = "input[value='Update Profile']"
    DROPDOWN = "a[class='dropdown-item']"
    NAVBAR = "a[class='navbar-brand']"
    PHOTO_ID = "customFile"

    UPDATE_PHOTO = "input[value='Update Photo']"

    USER_FIELDS = {
        'first_name_id': 'firstName',
        'last_name_id': 'lastName',
        'birthday_id': 'birthday',
        'email_id': 'email',
        'phone_id': 'phoneNumber',
        'country_id': 'country',
        'city_id': 'city',
        'street_id': 'street',
        'building_id': 'building',
        'apartment_id': 'apartment',
        'zipcode_id': 'zipCode'
        }




