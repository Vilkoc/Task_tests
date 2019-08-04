from init import BasePage
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.viewVacancy_page import ViewVacancyPage
from pages.viewCompany_page import ViewCompanyPage
from pages.companies_page import CompaniesPage


class TestSendClaim(BasePage):

    def test_send_claim(self, option1='Log in', person1='USER', option2='Log out', person2='ADMIN'):
        sign_in_page = SignInPage(self)

        self.header.select_option(option1)
        sign_in_page.login(person1)

        self.header.go_to_allVacancies()

        vacancies_page = VacanciesPage(self)
        vacancies_page.click_viewDetails_button()

        view_vacancy_page = ViewVacancyPage(self)
        view_vacancy_page.click_showCompany_button()

        view_company_page = ViewCompanyPage(self)
        view_company_page.click_claim_button()
        view_company_page.choose_option()
        view_company_page.fill_out_description_field('Text')
        view_company_page.click_send_claim_button()

        self.header.select_option(option2)
        sign_in_page.login(person2)

        companies_page = CompaniesPage(self)
        companies_page.click_show_claims_button()
        text = companies_page.description()

        assert text == 'Text'
