from locators import LocatorsHeader
from locators import LocatorsCreateCompanyPage
from locators import LocatorsMyCompaniesPage
from locators import LocatorsYourResume


class Header:
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
        """Verifies if the dropdown box appeared"""
        flag = self.browser.get_attr_value(self.locators.CHECK_DROPDOWN, 'aria-expanded')
        return True if flag == 'true' else False

    def click_log_out(self):
        """Clicks on the round icon"""
        self.browser.click_element_by_text_simple(self.locators.LOG_OUT)

    def click_log_in(self):
        """Clicks on the round icon"""
        self.browser.click_element_by_text_simple(self.locators.LOG_IN)

    def is_logined(self):
        """ Check if user logined: if 'logout' button exist == logined """
        self.click_icon()
        log_out = self.browser.get_elements_by_text(self.locators.LOG_OUT)
        return log_out.text == 'Log out'

    def select_option(self, pick_item):
        """The pick_item is default string parameter which accepts only 'Log in', 'Profile', 'Log out' values"""
        values = ('Log in', 'Profile', 'Log out')
        if pick_item not in values:
            raise Exception('Incorrect value for click_dropdown function')

       # if self.check_dropdown():
        url_0 = self.browser.driver.current_url
        while True:
            self.click_icon()
            print('clicked icon')
            while True:
                if self.check_dropdown():
                    print('dropdown available')
                    self.browser.click_element_by_text(self.locators.DROPDOWN, pick_item)
                    print('clicked', pick_item)
                    break
                else:
                    self.click_icon()
                    print('Emerge click icon')
            url_1 = self.browser.driver.current_url
            if url_0 != url_1:
                print('URL changed')
                break
            else:
                if pick_item == 'Log out':
                    if self.browser.get_text_of_element(self.locators.DROPDOWN) == 'Log in':
                        break


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
        self.browser.pause(PAUSE)
        return self.browser.get_elements(self.locators.LINKS)[1].text

    def go_to_allVacancies(self):
        self.browser.click_element_double_locator(self.locators_your_resume.SHOW_ALL_INFO_BUTTON,
                                                  self.locators.RABOTY_NET)
