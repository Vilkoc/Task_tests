from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Methods(object):
    """Webdriver wrapper"""
    def __init__(self, driver, default_timeout=10):
        self.driver = driver
        self.default_timeout = default_timeout

    def get_elements(self, locator):
        """Returns all elements for the specific locator"""
        return self.driver.find_elements(*locator)

    def get_elements_by_text(self, locator):
        """Returns element with specific text for the specific locator"""
        elements = self.driver.find_elements(*locator[0])
        for element in elements:
            if element.text == locator[1]:
                return element
        # test------------------------------------
        for number, element in enumerate(elements):
            print(number, element.text)
        raise 'No element for {}'.format(locator)
        # test ====================================

    def click_element(self, locator, elem_number=0):
        """Clicks on the element with number elem_number"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(locator))
        elements = self.get_elements(locator)
        elements[elem_number].click()

    def click_element_by_text(self, locator, text_value):
        """Clicks on the element with text attribute text_value"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(locator))
        elements = self.get_elements(locator)
        for element in elements:
            if element.text == text_value:
                element.click()

    def click_element_by_text_simple(self, locator_and_text):
        """Clicks on the element with text attribute text_value"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(locator_and_text[0]))
        elements = self.get_elements(locator_and_text[0])
        for element in elements:
            if element.text == locator_and_text[1]:
                element.click()

    def clear_element(self, locator, text_value='default'):
        """Clears the element with number elem_number"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
        elements = self.get_elements(locator)
        if text_value == 'default':
            elements[0].clear()

    def send_keys(self, locator, keys, text_value='default'):
        """Send keys to the element with number elem_number"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
        elements = self.get_elements(locator)
        if text_value == 'default':
            elements[0].send_keys(keys)

    def get_one_element(self, locator):
        """Returns element for the specific locator"""
        return self.driver.find_element(*locator)