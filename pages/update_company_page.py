from locators import LocatorsUpdateCompanyPage
from pages.create_company_page import CreateCompanyPage


class UpdateCompanyPage(CreateCompanyPage):
    """On this page company owner can update company information and save it"""

    def __init__(self, base_obj):
        super().__init__(base_obj)
        self.locators = LocatorsUpdateCompanyPage
        self.browser = base_obj.browser

    def update_company_name(self, company_name):
        self.browser.clear_element(LocatorsUpdateCompanyPage.COMPANY_NAME_TEXBOX)
        self.browser.send_keys(LocatorsUpdateCompanyPage.COMPANY_NAME_TEXBOX, company_name)

    def click_update_company_button(self):
        self.browser.click_element(LocatorsUpdateCompanyPage.UPDATE_COMPANY_BUTTON)

    def check_company_name(self):
        return self.browser.get_attr_value(self.locators.COMPANY_NAME_TEXBOX, "ng-reflect-model")
