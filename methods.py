from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Methods(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, numb_list=0, wait_id='PRESENCE'):
        """This function seeks for all elements for specific locator and returns only numb_list-th element"""
        # try:
        self.wait_for(locator, wait_id)
        element = self.driver.find_elements(*locator)
        return element[numb_list]
        # except:
        #     print("Exception on wait intercepted")
            #self.get_element(locator_type, locator, numb_list=0, wait_id='PRESENCE')


    def click_element(self, locator, numb_list=0, wait_id="PRESENCE"):
        element = self.get_element(locator, numb_list, wait_id)
        element.click()

    def clear_element(self, locator, numb_list=0, wait_id='PRESENCE'):
        element = self.get_element(locator, numb_list, wait_id)
        element.clear()

    def send_keys(self, locator, keys, numb_list=0, wait_id='PRESENCE'):
        element = self.get_element(locator, numb_list, wait_id)
        element.send_keys(keys)

    def wait_for(self, locator, wait_id='PRESENCE'):
        wait = WebDriverWait(self.driver, 10)
        if wait_id == 'PRESENCE':
            wait.until(EC.presence_of_all_elements_located(locator))
        elif wait_id == 'VISIBLE':
            wait.until(EC.visibility_of_element_located(locator))
        elif wait_id == 'CLICKABLE':
            wait.until(EC.element_to_be_clickable(locator))
        else:
            print('Incorrect WAITER, the default is used')
            wait.until(EC.presence_of_all_elements_located(locator))
            
