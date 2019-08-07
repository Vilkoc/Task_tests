from init import BasePage
from pages.auth_page import AuthPage
from pages.vacancies_page import VacanciesPage
from config import EMAIL_SUBJECT_SIGNUP, USERNAME_SIGNUP, PASSWORD, EMAIL_SIGNUP, FROM_SIGNUP
from utilities.get_email import get_link


class TestSignUp(BasePage):

    def test_sign_up(self):
        page = AuthPage(self)
        vacancies = VacanciesPage(self)

        self.header.click_icon()
        self.header.click_log_in()

        page.click_sign_up_tab()

        page.enter_sign_up_email(USERNAME_SIGNUP)
        page.enter_sign_up_password(PASSWORD)
        page.enter_sign_up_matching_password(PASSWORD)
        page.click_sing_up_button()

        assert vacancies.is_confirmation_sent()

        link = get_link(EMAIL_SIGNUP, FROM_SIGNUP, EMAIL_SUBJECT_SIGNUP)
        vacancies.click_confirmation_link(link)

        page.login_user(USERNAME_SIGNUP, PASSWORD)
        assert self.header.is_logined()
