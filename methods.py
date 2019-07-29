from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Methods(object):
    """Webdriver wrapper"""
    def __init__(self, driver):
        self.driver = driver

    def get_elements(self, locator):
        """Returns all elements for the specific locator"""
        return self.driver.find_elements(*locator)

    def click_element(self, locator, elem_number=0):
        """Clicks on the element with number elem_number"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        elements = self.get_elements(locator)
        elements[elem_number].click()

    def click_element_by_text(self, locator, text_value):
        """Clicks on the element with text attribute text_value"""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        elements = self.get_elements(locator)
        for element in elements:
            if element.text == text_value:
                element.click()

    def clear_element(self, locator, elem_number=0):
        """Clears the element with number elem_number"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        elements = self.get_elements(locator)
        elements[elem_number].clear()

    def send_keys(self, locator, keys, elem_number=0):
        """Send keys to the element with number elem_number"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        elements = self.get_elements(locator)
        elements[elem_number].send_keys(keys)