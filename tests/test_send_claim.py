from init import BasePage
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.view_vacancy_page import ViewVacancyPage
from pages.view_company_page import ViewCompanyPage
from pages.companies_page import CompaniesPage
from data_tests import test_data_Nazar as td


class TestSendClaim(BasePage):

    def test_send_claim(self):
        sign_in_page = SignInPage(self)

        self.header.select_option(td.LOG_IN)
        sign_in_page.login(td.USER)

        self.header.go_to_allVacancies()

        vacancies_page = VacanciesPage(self)
        vacancies_page.click_viewDetails_button()

        view_vacancy_page = ViewVacancyPage(self)
        view_vacancy_page.click_showCompany_button()

        view_company_page = ViewCompanyPage(self)
        view_company_page.click_claim_button()
        view_company_page.choose_option()
        view_company_page.fill_out_description_field(td.DESCRIPTION)
        view_company_page.click_send_claim_button()

        self.header.select_option(td.LOG_OUT)
        sign_in_page.login(td.ADMIN)

        companies_page = CompaniesPage(self)
        companies_page.click_show_claims_button()
        text = companies_page.description()

        assert text == td.DESCRIPTION
