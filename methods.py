from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Methods(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_type, locator, numb_list=0):
        # This function seeks for elements
        types_By = {
            'id': By.ID,
            'css': By.CSS_SELECTOR}
        element = self.driver.find_elements(types_By[locator_type], locator)
        return element[numb_list]

    def click_element(self, locator_type, locator, numb_list=0):
        element = self.get_element(locator_type, locator, numb_list)
        element.click()


    def clear_element(self, locator_type, locator):
        element = self.get_element(locator_type, locator)
        element.clear()

    def send_keys(self, locator_type, locator, keys):
        element = self.get_element(locator_type, locator)
        element.send_keys(keys)


            
