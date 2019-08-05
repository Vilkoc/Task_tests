from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class DriverWrapper(object):
    """Webdriver wrapper"""

    def __init__(self, driver, default_timeout=10):
        self.driver = driver
        self.default_timeout = default_timeout

    def get_elements(self, locator):
        """Returns all elements for the specific locator"""
        return self.driver.find_elements(*locator)

    def get_one_element(self, locator):
        """Returns element for the specific locator"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_one_element(self, locator):
        """Clicks on the element with number elem_number"""
        # WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(locator))
        element = self.get_one_element(locator)
        element.click()

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

    def click_element_by_text_simple(self, locator_and_text):
        """Clicks on the element with text attribute text_value"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(locator_and_text[0]))
        elements = self.get_elements(locator_and_text[0])
        for element in elements:
            if element.text == locator_and_text[1]:
                element.click()

    def clear_element(self, locator, text_value='default'):
        """Clears the element with the specific text_value"""
        WebDriverWait(self.driver, self.default_timeout).until(EC.presence_of_element_located(locator))
        elements = self.get_elements(locator)
        if text_value == 'default':
            elements[0].clear()
        else:
            for element in elements:
                if element.text == text_value:
                    element.clear()

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
        WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locator))
        element = self.get_elements(locator)[0]
        return element.get_attribute(attr)

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

    def get_text_of_element(self, locator):
        return self.get_one_element(locator).text

    def pause(self, time):
        webdriver.support.wait.time.sleep(time)



