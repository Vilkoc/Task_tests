from locators import LocatorsHeader
from locators import LocatorsYourResume



class Header():
    """Header page, which will be inherited by other pages"""

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators_header = LocatorsHeader
        self.locators_your_resume = LocatorsYourResume


    def click_icon(self):
        self.browser.click_element(self.locators_header.ICON)

    def check_dropdown(self):
        flag = self.browser.get_attr_value(self.locators_header.CHECK_DROPDOWN, 'aria-expanded')
        return flag == 'true'

    def select_option(self, pick_item):
        values = ('Log in', 'Profile', 'Log out')
        if pick_item not in values:
            raise Exception('Incorrect value for click_dropdown function')
        self.click_icon()
        if self.check_dropdown():
            self.browser.click_element_by_text(self.locators_header.DROPDOWN, pick_item)
        else:
            self.click_icon()

    def person_verify(self, person):
        person_criteria = {'ADMIN': 3, 'USER': 4, 'COWNER': 6}
        default_person = 2
        while default_person < person_criteria[person]:
            default_person = len(self.browser.get_elements(self.locators_header.NAVBAR))
        if len(self.browser.get_elements(self.locators_header.NAVBAR)) == person_criteria[person]:
            return True
        return False

    def go_to_allVacancies(self):
        self.browser.click_element_double_locator(self.locators_your_resume.SHOW_ALL_INFO_BUTTON,
                                                  self.locators_header.RABOTY_NET)
