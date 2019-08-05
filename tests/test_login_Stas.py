from init import BasePage
from parameterized import parameterized
from pages.auth_page import AuthPage
from data_tests import auth as td


class TestLogin(BasePage):
    @parameterized.expand(td.LOGIN)
    def test_login_logout(self, user, password, expected_result):
        page = AuthPage(self)

        self.header.click_icon()
        self.header.click_log_in()

        page.enter_sign_in_email(user)
        page.enter_sign_in_password(password)
        page.click_sign_in()

        assert self.header.get_text_of_first_link() == expected_result

        self.header.click_icon()
        self.header.click_log_out()
