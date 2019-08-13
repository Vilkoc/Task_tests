from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from config import TIMEOUT


class DriverWrapper(object):
    """Webdriver wrapper"""

    def __init__(self, driver, default_timeout=30):
        self.driver = driver
        self.default_timeout = default_timeout

    def get_element(self, locator):
        """Returns all elements for the specific locator"""
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        """Returns all elements for the specific locator"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def get_elements_by_text(self, locator):
        """Returns element with specific text for the specific locator"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(locator[0]))
        elements = self.driver.find_elements(*locator[0])
        for element in elements:
            if element.text == locator[1]:
                return element

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

    def clear_element(self, locator):
        """Clears the element with the specific text_value"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
        self.get_element(locator).clear()

    def get_text_of_element(self, locator):
        """ Get text from element """
        WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locator))
        return self.get_element(locator).text

    def send_keys(self, locator, keys, text_value='default'):
        """Send keys to the element with the the specific text_value"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
        elements = self.get_elements(locator)
        if text_value == 'default':
            elements[0].send_keys(keys)
        else:
            for element in elements:
                if element.text == text_value:
                    element.send_keys(keys)

    def get_attr_value(self, locator, attr):
        """Get attribute value of the element"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
        element = self.get_element(locator)
        return element.get_attribute(attr)

    def click_element_double_locator(self, locator_wait, locator_element):
        """This function takes two locators, first one for 'WebDriverWait', the second one for click on the element"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locator_wait))
        element = self.get_element(locator_element)
        element.click()

    def click_button_change(self, locator_buttons, locator_wait):
        """Special function for press 'Change' button"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locator_wait))
        buttons = self.get_elements(locator_buttons)
        change = None
        for i in buttons:
            if i.text == 'Change':
                change = i
        change.click()

    def invisibility_of_element(self, locator):
        """This function wait until element will be invisible"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.invisibility_of_element(locator))

    def wait_element_with_text(self, locator, text, timeout=TIMEOUT):
        """ Wait while element with certain text appears """
        end = time.time() + timeout

        while time.time() < end:
            elements = self.get_elements(locator)
            for element in elements:
                try:
                    if element.text == text:
                        return element
                except:
                    pass
        print('====data:', locator, text)
        raise Exception("Time out to find element")

    def wait_of_quantity_elements(self, locator, quantity, timeout=TIMEOUT):
        """ Wait while on page will be certain quantity of elements"""
        end = time.time() + timeout
        while time.time() < end:
            elements = self.get_elements(locator)
            if len(elements) >= quantity:
                return
        print('====data:', locator, quantity, len(elements))
        raise Exception("No enougth elements")

    def company_view_update_delete(self, locator1, locator2, company_name):
        """This function clicks on company details/update/delete buttons
         according to the company name and specific locators"""
        tbody = self.driver.find_elements(*locator1)
        for i in tbody:
            if company_name in i.text:
                td = i.find_element(*locator2)
                td.click()

    def read_data_in_textbox(self, locator_list, locator_attribute):
        """Gets values from the input fields by attribute and return a list of this values"""
        data_list = []
        for el in range(len(locator_list)):
            a = self.driver.find_element_by_id(locator_list[el]).get_attribute(
                locator_attribute)
            data_list.append(a)
        return data_list

    def get_element_with_time_delay(self, locator):
        """Returns all elements for the specific locator"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def pop_up_element(self, locator):
        """Returns element from pop-up window"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_property_wrapper(self, locator, prop):
        """Returns True if property is present"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
        element = self.get_elements(locator)[0]
        return element.get_property(prop)

    def get_element_with_time_delay(self, locator):
        """Returns all elements for the specific locator"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)