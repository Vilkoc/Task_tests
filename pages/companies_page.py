from locators import LocatorsCompaniesPage


class CompaniesPage():
    """On this page admin can moderate companies"""

    def __init__(self, base_obj):
        self.browser = base_obj.browser
        self.locators = LocatorsCompaniesPage

    def view_detail_about_co(self):
        self.browser.click_element(self.locators.DETAILS_ABOUT_CO)

    def view_status_of_co(self):
        tmp1 = self.browser.get_attr_value(self.locators.STATUS_APPROVED, 'title')
        return tmp1 == 'This company is approved'

    def view_warning_status_of_co(self):
        tmp1 = self.browser.get_attr_value(self.locators.STATUS_WARNING, 'title')
        return tmp1 == 'This company has claims'

    def block_co(self):
        self.browser.click_element(self.locators.BLOCK_1_CO)

    def unblock_co(self):
        self.browser.click_element(self.locators.UNBLOCK_2_CO)

    def approve_co(self):
        self.browser.click_element(self.locators.APPROVE_CO)

    def reject_claim(self):
        self.browser.click_element(self.locators.REJECT_CLAIM_BTN)

    def confirm_with_popup(self):
        tmp = self.browser.driver.get_element(self.locators.POPUP)
        tmp2 = tmp.find_element_by_tag_name('p').text
        return tmp2
