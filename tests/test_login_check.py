from init import SeleniumTestBase


class TestLoginAll(SeleniumTestBase):

    def setUp(self):
        self.header.select_option('Log in')

    def test_login_admin(self, person="ADMIN"):
        self.sign_in_page.login(person)
        assert self.header.person_verify(person)

    def test_login_user(self, person="USER"):
        self.sign_in_page.login(person)
        assert self.header.person_verify(person)

    def test_login_cowner(self, person="COWNER"):
        self.sign_in_page.login(person)
        assert self.header.person_verify(person)

    def tearDown(self):
        self.header.select_option('Log out')


