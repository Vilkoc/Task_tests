from init import BasePage
from pages.sign_in_page import SignInPage
from pages.user_profile_page import UserPage
import time


class TestUpdateProfile(BasePage):

    def test_update_profile(self, person='USER'):
        driver = self.driver

        SignInPage(driver).login(person)
        time.sleep(2)

        user_page = UserPage(driver)
        user_page.transmit('Profile')
        time.sleep(2)

        user_page.click_update_profile()

        user_page.transmit('Log out')
        

if __name__ == "__main__":
    unittest.main()
