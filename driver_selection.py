from selenium import webdriver


class WebdriverSelection():
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name.lower() == 'chrome':
            return webdriver.Chrome()
        elif browser_name.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser_name.lower() == 'ie':
            return webdriver.ie
        elif browser_name.lower() == 'opera':
            return webdriver.Opera()
        else:
            raise Exception("There's no available driver for such browser")

