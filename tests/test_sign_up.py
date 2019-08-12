from data_tests.auth import USERNAME_SIGNUP, PASSWORD
from init import SeleniumTestBase
from utilities.func import login
from utilities.db import change_varification_link, wait_user_update


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

        change_varification_link(USERNAME_SIGNUP)
        link = 'http://localhost:4200/users/auth/confirm?token=3e83667c-c59c-4fda-aa7a-a47346a3cd6a'
        self.vacancies.click_confirmation_link(link)

        wait_user_update(USERNAME_SIGNUP)

        login(self.browser, USERNAME_SIGNUP, PASSWORD)
        assert self.header.is_logined()
