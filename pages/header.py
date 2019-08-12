from locators import LocatorsHeader, LocatorsCreateCompanyPage, LocatorsMyCompaniesPage
from locators import LocatorsYourResume


class Header():
    """Header page, which will be inherited by other pages"""
    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsHeader
        self.locator_create_company = LocatorsCreateCompanyPage
        self.locator_my_companies = LocatorsMyCompaniesPage
        self.locators_your_resume = LocatorsYourResume

    def click_icon(self):
        """Clicks on the round icon"""
        self.browser.click_element(self.locators.ICON)

    def check_dropdown(self):
        flag = self.browser.get_attr_value(self.locators.CHECK_DROPDOWN, 'aria-expanded')
        return flag == 'true'

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

    def click_log_out(self):
        """Clicks on the round icon"""
        self.browser.click_element_by_text(self.locators.LOG_OUT, "Log out")

    def click_log_in(self):
        """Clicks on the round icon"""
        self.browser.wait_element_with_text(self.locators.LOG_IN, "Log in")
        self.browser.click_element_by_text(self.locators.LOG_IN, "Log in")

    def is_logined(self):
        """ Check if user logined: if 'logout' button exist == logined """
        self.click_icon()
        log_out = self.browser.wait_element_with_text(self.locators.LOG_OUT, "Log out")
        return log_out.text == 'Log out'

    def person_verify(self, person):
        """Returns True if the number of elements on the navbar equals to the person_criteria"""
        person_criteria = {'ADMIN': 3, 'USER': 4, 'COWNER': 6}
        current_person = 2
        while current_person < person_criteria[person]:
            current_person = len(self.browser.get_elements(self.locators.NAVBAR))
        return True if current_person == person_criteria[person] else False

    def move_to_companies(self):
        self.browser.click_element(self.locators.MOVE_TO_COMPANIES)

    def click_create_company(self):
        self.browser.click_element(self.locator_create_company.CREATE_COMPANY_TAB)

    def click_my_companies(self):
        self.browser.click_element(self.locator_my_companies.MY_COMPANIES)

    def get_text_of_first_link(self):
        self.browser.wait_of_quantity_elements(self.locators.LINKS, 3)
        return self.browser.get_elements(self.locators.LINKS)[1].text

    def go_to_allVacancies(self):
        self.browser.click_element_double_locator(self.locators_your_resume.SHOW_ALL_INFO_BUTTON,
                                                  self.locators.RABOTY_NET)
