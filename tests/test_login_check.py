from init import BasePage
from pages.sign_in_page import SignInPage
from pages.header import Header
from credentials import Credentials


class TestLoginAll(BasePage):

    def test_login_all(self):
        driver = self.driver
        for person in Credentials.keys():
            inquire = Header(driver)
            sign_in = SignInPage(driver)

            sign_in.login(person)
            assert inquire.person_verify(person)
            inquire.select_option('Log out')


if __name__ == "__main__":
    main()
