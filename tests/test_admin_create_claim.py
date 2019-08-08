from init import SeleniumTestBase
from pages.companies_page import CompaniesPage
from pages.company_details_page import CompanyDetailsPage
from pages.header import Header
from pages.sign_in_page import SignInPage


class TestAdminCreateClaim(SeleniumTestBase):

    def test_admin_create_claim(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('ADMIN')
        self.companies_page.view_detail_about_co()

        self.company_details_page.create_claim()
        self.company_details_page.select_title_of_claim()
        self.company_details_page.set_description_of_claim()
        self.company_details_page.send_claim()
        self.header.move_to_companies()

        assert self.companies_page.view_warning_status_of_co()
