from methods import Methods
from locators import Locators

class HomePage:
    """Home page description, is parent for UserPage"""
    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)
        self.locators = Locators


    def click_icon(self):
        self.methods.click_element('css', self.locators.icon)

    def click_login(self):
        self.methods.click_element('css', self.locators.login)

    def clear_box(self, box_name):
        self.methods.clear_element('id', self.locators.id_loc[box_name])

    def send_keys(self, box_name, keys):
        self.methods.send_keys('id', self.locators.id_loc[box_name], keys)

    def click_sign_in(self):
        self.methods.click_element('css', self.locators.sign_in)




##
##class SignInPage:
##    """Sign in page, it also checks if sign in is complete"""
##    def __init__(self, driver):
##        self.driver = driver
##        self.email_field = Locators.email_sign_in_id
##        self.password_field = Locators.password_link_id
##        self.sign_in_button = Locators.sign_in_css_selector
##        self.nav_bar = Locators.navbar_css_selector
##
##    def enter_email(self, user_email):
##        self.driver.find_element(By.ID, self.email_field).clear()
##        self.driver.find_element(By.ID, self.email_field).send_keys(user_email)
##
##    def enter_password(self, password):
##        self.driver.find_element(By.ID, self.password_field).clear()
##        self.driver.find_element(By.ID, self.password_field).send_keys(password)
##
##    def click_sign_in(self):
##        elem_1 = self.driver.find_element(By.CSS_SELECTOR, self.sign_in_button)
##        elem_1.click()
##        elem_2 = self.driver.find_elements(By.CSS_SELECTOR, self.nav_bar)
##        while len(elem_2) <= 2: #Checking if SignIn finished
##            elem_2 = self.driver.find_elements(By.CSS_SELECTOR, self.nav_bar)
##
##
##class UserPage(HomePage):
##    """User Page, inherits from HomePage"""
##    def __init__(self, driver):
##        super().__init__(driver)
##       # self.profile_button = Locators.profile_btn_xpath
##        self.dropdown = Locators.dropdown_css_selector
##        self.photo_field = Locators.photo_id
##        self.update_photo_btn = Locators.update_photo_css_selector
##        self.update_profile = Locators.update_profile_css_selector
##        self.nav_bar = Locators.navbar_css_selector
##        self.user_fields = Locators.user_fields_id
##        self.nav_bar = Locators.navbar_css_selector
###        self.photo_place = Locators.photo_place_xpath
##
##    def click_profile(self):
##        elem = self.driver.find_elements(By.CSS_SELECTOR, self.dropdown)
##        elem[0].click()
##
##    def click_logout(self):
##        try:
##            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dropdown)))
##            elem = self.driver.find_elements(By.CSS_SELECTOR, self.dropdown)
##            elem[1].click()
##        except:
##            print('logout failed')
##            self.click_icon()
##
##    def click_navbar(self):
##        elem_1 = self.driver.find_elements(By.CSS_SELECTOR, self.nav_bar)
##        elem_1[1].click()
##
##    def click_update_profile(self):
##        self.driver.find_element(By.CSS_SELECTOR, self.update_profile).click()
##
##
##    def click_update_photo(self, photo_file):
##        self.driver.find_element(By.ID, self.photo_field).send_keys(photo_file)
##        self.driver.execute_script('window.scrollTo(0,0)')
##        self.driver.find_element(By.CSS_SELECTOR, self.update_photo_btn).click()
##
##
##    def enter_user_data(self, key_id, data_entry):
##        try:
##            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.user_fields[key_id])))
##            element = self.driver.find_element(By.ID, self.user_fields[key_id])
##            element.clear()
##            element.send_keys(data_entry)
##            if 'ng-invalid' in element.get_attribute('class'):
##                return False
##            else:
##                return True
##        except:
##            print('Extra processing of', key_id)
##            self.enter_user_data(key_id, data_entry)
##
##    def read_user_data(self, key_id):
##        while True:
##            try:
##                element = self.driver.find_element(By.ID, self.user_fields[key_id])
##                temp = element.get_attribute('ng-reflect-model')
##                break
##            except:
##                print('Extra processing of read of', key_id)
##        return temp
##
##    # def compare_pics(self):
##    #     try:
##    #
##    #     elem_1 = self.driver.find_element(By.XPATH, self.photo_place)
##    #     elem_2 = self.driver.find_element(By.CLASS_NAME, self.icon_link)
##    #     if elem_1.get_attribute('src') == elem_2.get_attribute('src'):
##    #         return True
##    #     else:
##    #         return False
##
