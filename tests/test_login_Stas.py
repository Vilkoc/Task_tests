from init import SeleniumTestBase
from parameterized import parameterized

class TestLogin(SeleniumTestBase):
    @parameterized.expand([
        ('admin@gmail.com', 'admin', 'Сompanies'),
        ('user@gmail.com', 'user', 'Create company'),
        ('cowner@gmail.com', 'cowner', 'My companies')
    ])
    def test_login_logout(self, user, password, expected):

        self.header.click_icon()
        self.header.click_log_in()

        self.sign_in_page.enter_sign_in_email(user)
        self.sign_in_page.enter_sign_in_password(password)
        self.sign_in_page.click_sign_in()

        assert self.header.get_text_of_first_link() == expected

        self.header.click_icon()
        self.header.click_log_out()
