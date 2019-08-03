from init import BasePage

from pages.auth_page import AuthPage

USER = 'user@gmail.com'
PASS = 'user'


class TestLogin(BasePage):

    def test_login_logout(self):
        page = AuthPage(self)

        self.header.click_icon()
        self.header.click_log_in()

        page.enter_sign_in_email(USER)
        page.enter_sign_in_password(PASS)
        page.click_sign_in()

        assert self.header.is_logined()