from init import BasePage
import unittest
from parameterized import parameterized

from pages.auth_page import AuthPage

USER = 'user@gmail.com'
PASS = 'user'


class TestLogin(BasePage):
    @parameterized.expand([
        ('admin@gmail.com', 'admin', 'Сompanies'),
        ('user@gmail.com', 'user', 'Create company'),
        ('cowner@gmail.com', 'cowner', 'My companies')
    ])
    def test_login_logout(self, user, password, expected):
        page = AuthPage(self)

        self.header.click_icon()
        self.header.click_log_in()

        page.enter_sign_in_email(user)
        page.enter_sign_in_password(password)
        page.click_sign_in()

        assert self.header.get_text_of_first_link() == expected

        self.header.click_icon()
        self.header.click_log_out()

