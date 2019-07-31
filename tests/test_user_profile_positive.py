from init import BasePage
from pages.sign_in_page import SignInPage
from pages.user_profile_page import UserPage
from user_data import user_data_rab_19 as entry
import time


class TestPositive(BasePage):

    def test_positive(self, person='USER'):
        driver = self.driver

        SignInPage(driver).login(person)
        time.sleep(2)

        user_page = UserPage(driver)
        user_page.transmit('Profile')

        for key in entry.keys():
            user_page.enter_data_textbox(key, entry[key])

        time.sleep(2)
        user_page.click_update_profile()

        time.sleep(2)
        for key in entry.keys():
            if key == 'BIRTHDAY':
                tmp = entry[key]
                entry[key] = tmp[2] + '-' + tmp[0] + '-' + tmp[1]
            assert entry[key] == user_page.read_data_textbox(key)



        user_page.transmit('Log out')
        

if __name__ == "__main__":
    unittest.main()
