from init import BasePage
import unittest
from pages.header import Header
from pages.auth_page import AuthPage
from config import EMAIL_SUBJECT_SIGNUP, USERNAME_SIGNUP, PASSWORD

class TestSignUp(BasePage):

    def test_(self):
        header = Header(self.driver)
        page = AuthPage(self.driver)


        header.click_icon()
        header.click_log_in()

        page.click_sign_up_tab()

        page.enter_sign_up_email(USERNAME_SIGNUP)
        page.enter_sign_up_password(PASSWORD)
        page.enter_sign_up_matching_password(PASSWORD)

        page.click_sing_up_button()

        assert page.is_logined()

if __name__ == "__main__":
    unittest.main()
