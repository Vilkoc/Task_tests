from init import SeleniumTestBase


class TestSendClaim(SeleniumTestBase):

    def setUp(self):
        self.header.select_option("Log in")
        self.sign_in_page.login("USER")

    def test_send_claim(self):
        self.header.go_to_allVacancies()

        self.vacancies_page.click_viewDetails_button()

        self.view_vacancy_page.click_showCompany_button()

        self.view_company_page.click_claim_button()
        self.view_company_page.choose_option()
        self.view_company_page.fill_out_description_field("Text")
        self.view_company_page.click_send_claim_button()

        self.header.select_option("Log out")
        self.header.select_option("Log in")
        self.sign_in_page.login("ADMIN")

        self.companies_page.click_show_claims_button()
        text = self.companies_page.description()

        assert text == "Text"
