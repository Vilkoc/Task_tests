class Locators:

    icon = "img[class='rounded-circle img-responsive z-depth-0']"
    login = "a[href='/users/auth']"
    id_loc = {
        'email': "username",
        'password': "password"
    }
    sign_in = "input[value='Sign In']"


class LocatorsUsers:

    update_profile_css_selector = "input[value='Update Profile']"
    dropdown_css_selector = "a[class='dropdown-item']"
    navbar_css_selector = "a[class='navbar-brand']"
    photo_id = "customFile"

    update_photo_css_selector = "input[value='Update Photo']"

    user_fields_id = {
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

