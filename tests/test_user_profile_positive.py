from init import BasePage
from pages.sign_in_page import SignInPage
from pages.user_profile_page import UserPage
from user_data import user_data_rab_19 as entry


class TestPositive(BasePage):

    def test_user_profile_positive(self, person='COWNER'):

        start = SignInPage(self)
        perform = UserPage(self)

        start.login(person)
        self.header.select_option('Profile')

        for key in entry.keys():
            perform.enter_data_textbox(key, entry[key])

        perform.click_update_profile()
        self.browser.driver.save_screenshot('sample.png')

        for key in entry.keys():
            if key == 'BIRTHDAY':
                tmp = entry[key]
                entry[key] = tmp[2] + '-' + tmp[0] + '-' + tmp[1]
            assert entry[key] == perform.read_data_textbox(key)

        self.header.select_option('Log out')
