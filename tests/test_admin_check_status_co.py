from init import SeleniumTestBase


class TestAdminCheckStatusCo(SeleniumTestBase):

    def test_admin_check_status_co(self):
        self.header.select_option('Log in')
        self.sign_in_page.login('ADMIN')

        assert self.companies_page.view_status_of_co()
