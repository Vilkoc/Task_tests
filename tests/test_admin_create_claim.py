from init import BasePage
from pages.companies_page import CompaniesPage
from pages.company_details_page import CompanyDetailsPage
from pages.header import Header
from pages.sign_in_page import SignInPage


class TestAdminCreateClaim(BasePage):
    def test_login_logout(self, person='ADMIN'):
        signin = SignInPage(self)
        signin.login(person)
        companies = CompaniesPage(self)
        companies.view_detail_about_co()
        details = CompanyDetailsPage(self)
        details.create_claim()
        details.select_title_of_claim()
        details.set_description_of_claim()
        details.send_claim()
        header = Header(self)
        header.move_to_companies()
        assert companies.view_warning_status_of_co()
