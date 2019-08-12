from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.view_vacancy_page import ViewVacancyPage
from pages.view_company_page import ViewCompanyPage
from pages.companies_page import CompaniesPage
import pytest
from init import setup


@pytest.mark.usefixtures('setup')
class TestSendClaim:

    def test_send_claim(self):
        self.header = Header(self.browser)
        self.sign_in_page = SignInPage(self.browser)
        self.vacancies_page = VacanciesPage(self.browser)
        self.view_vacancy_page = ViewVacancyPage(self.browser)
        self.view_company_page = ViewCompanyPage(self.browser)
        self.companies_page = CompaniesPage(self.browser)

        self.header.select_option("Log in")
        self.sign_in_page.login("USER")

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
