from locators import LocatorsHeader


class Header():
    """Header page, which will be inherited by other pages"""

    def __init__(self, base_obj):
        self.browser = base_obj.browser

        self.locators = LocatorsHeader

    def click_icon(self):
        """Clicks on the round icon"""
        self.browser.click_element(self.locators.ICON)

    def check_dropdown(self):
        flag = self.browser.get_attr_value(self.locators.CHECK_DROPDOWN, 'aria-expanded')
        return flag == 'true'

    def check_dropdown(self):
        flag = self.get_attr_value(self.locators.CHECK_DROPDOWN, 'aria-expanded')
        if flag == 'true':
            return True
        else:
            return False

    def select_option(self, pick_item):
        """The pick_item is default string parameter which accepts only 'Log in', 'Profile', 'Log out' values"""
        values = ('Log in', 'Profile', 'Log out')
        if pick_item not in values:
            raise Exception('Incorrect value for click_dropdown function')
        self.click_icon()
        if self.check_dropdown():

            self.browser.click_element_by_text(self.locators.DROPDOWN, pick_item)
        else:
            self.click_icon()

    def person_verify(self, person):
        """Returns True if the number of elements on the navbar equals to person_criteria"""
        person_criteria = {'ADMIN': 3, 'USER': 4, 'COWNER': 6}
        default_person = 2
        while default_person < person_criteria[person]:
            default_person = len(self.browser.get_elements(self.locators.NAVBAR))
        if len(self.browser.get_elements(self.locators.NAVBAR)) == person_criteria[person]:
            return True
        return False
