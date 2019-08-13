from init import SeleniumTestBase


class TestAdmin(SeleniumTestBase):

    def test_admin_companies_presence(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('ADMIN')

        assert self.companies_page.companies_are_visible()
