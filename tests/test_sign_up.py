from init import BasePage
from pages.auth_page import AuthPage
from pages.vacancies_page import VacanciesPage
from data_tests import auth as td
from utilities.get_email import get_link


class TestSignUp(BasePage):

    def test_sign_up(self):
        page = AuthPage(self)
        vacancies = VacanciesPage(self)

        self.header.click_icon()
        self.header.click_log_in()

        page.click_sign_up_tab()

        page.enter_sign_up_email(td.USERNAME_SIGNUP)
        page.enter_sign_up_password(td.PASSWORD)
        page.enter_sign_up_matching_password(td.PASSWORD)
        page.click_sing_up_button()

        assert vacancies.is_confirmation_sent()

        link = get_link(td.EMAIL_SIGNUP, td.FROM_SIGNUP, td.EMAIL_SUBJECT_SIGNUP)
        vacancies.click_confirmation_link(link)

        page.login_user(td.USERNAME_SIGNUP, td.PASSWORD)
        assert self.header.is_logined()
