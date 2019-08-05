from locators import LocatorsHeader


class Header:
    """Header page, which will be inherited by other pages"""

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsHeader

    def click_icon(self):
        """Clicks on the round icon"""
        self.browser.click_element(self.locators.ICON)

    def check_dropdown(self):
        """Verifies if the dropdown box appeared"""
        flag = self.browser.get_attr_value(self.locators.CHECK_DROPDOWN, 'aria-expanded')
        return True if flag == 'true' else False

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
        """Returns True if the number of elements on the navbar equals to the person_criteria"""
        person_criteria = {'ADMIN': 3, 'USER': 4, 'COWNER': 6}
        current_person = 2
        while current_person < person_criteria[person]:
            current_person = len(self.browser.get_elements(self.locators.NAVBAR))
        return True if current_person == person_criteria[person] else False
