from init import BasePage
from pages.sign_in_page import SignInPage
from credentials import Credentials


class TestLoginAll(BasePage):

    def test_login_all(self):
        driver = self.driver
        for person in Credentials.keys():
            inquire = SignInPage(driver)

            inquire.login(person)
            assert inquire.header.person_verify(person)
            inquire.header.select_option('Log out')


if __name__ == "__main__":
    main()
