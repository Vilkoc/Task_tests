from methods import Methods
from pages.header import Header
from locators import LocatorsUserPage


class UserPage(Methods):
    """User Page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LocatorsUserPage

    def transmit(self, pick_item):
        return Header(self.driver).transit(pick_item)


    # def click_navbar(self):
    #     elem_1 = self.driver.find_elements(By.CSS_SELECTOR, self.nav_bar)
    #     elem_1[1].click()

    def click_update_profile(self):
        self.click_element(self.locators.UPDATE_PROFILE)


    # def click_update_photo(self, photo_file):
    #     self.driver.find_element(By.ID, self.photo_field).send_keys(photo_file)
    #     self.driver.execute_script('window.scrollTo(0,0)')
    #     self.driver.find_element(By.CSS_SELECTOR, self.update_photo_btn).click()


    # def enter_user_data(self, key_id, data_entry):
    #     try:
    #         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.user_fields[key_id])))
    #         element = self.driver.find_element(By.ID, self.user_fields[key_id])
    #         element.clear()
    #         element.send_keys(data_entry)
    #         if 'ng-invalid' in element.get_attribute('class'):
    #             return False
    #         else:
    #             return True
    #     except:
    #         print('Extra processing of', key_id)
    #         self.enter_user_data(key_id, data_entry)
    #
    # def read_user_data(self, key_id):
    #     while True:
    #         try:
    #             element = self.driver.find_element(By.ID, self.user_fields[key_id])
    #             temp = element.get_attribute('ng-reflect-model')
    #             break
    #         except:
    #             print('Extra processing of read of', key_id)
    #     return temp

    # def compare_pics(self):
    #     try:
    #
    #     elem_1 = self.driver.find_element(By.XPATH, self.photo_place)
    #     elem_2 = self.driver.find_element(By.CLASS_NAME, self.icon_link)
    #     if elem_1.get_attribute('src') == elem_2.get_attribute('src'):
    #         return True
    #     else:
    #         return False

