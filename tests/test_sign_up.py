from pages.auth_page import AuthPage
from pages.vacancies_page import VacanciesPage
from data_tests.auth import EMAIL_SUBJECT_SIGNUP, USERNAME_SIGNUP, PASSWORD, EMAIL_SIGNUP, FROM_SIGNUP
from init import SeleniumTestBase
from utilities.get_email import get_link


class TestSignUp(SeleniumTestBase):

    def test_sign_up(self):
        self.header.click_icon()
        self.header.click_log_in()

        self.sign_in_page.click_sign_up_tab()

        self.sign_in_page.enter_sign_up_email(USERNAME_SIGNUP)
        self.sign_in_page.enter_sign_up_password(PASSWORD)
        self.sign_in_page.enter_sign_up_matching_password(PASSWORD)
        self.sign_in_page.click_sing_up_button()

        assert self.vacancies.is_confirmation_sent()

        link = get_link(EMAIL_SIGNUP, FROM_SIGNUP, EMAIL_SUBJECT_SIGNUP)
        self.vacancies.click_confirmation_link(link)

        self.sign_in_page.login_user(USERNAME_SIGNUP, PASSWORD)
        assert self.header.is_logined()
