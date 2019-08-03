from locators import LocatorsUpdateCompanyPage
from pages.create_company_page import CreateCompanyPage


class UpdateCompanyPage(CreateCompanyPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LocatorsUpdateCompanyPage

    def update_company_name(self, company_name):
        self.clear_element(LocatorsUpdateCompanyPage.COMPANY_NAME_TEXBOX)
        self.send_keys(LocatorsUpdateCompanyPage.COMPANY_NAME_TEXBOX, company_name)

    def click_update_company_button(self):
        self.click_element(LocatorsUpdateCompanyPage.UPDATE_COMPANY_BUTTON)
