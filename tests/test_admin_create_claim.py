from init import SeleniumTestBase


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
