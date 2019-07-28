from methods import Methods
from locators import Locators

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods(self.driver)
        self.locators = Locators


    def click_icon(self):
        self.methods.click_element(self.locators.ICON)

    def click_dropdown(self, numb_list=0):
        """This function clicks on dropdown menu:
        numb_list=0 - stays for:
         Login in Guest, Profile in User/Cowner, Logout in Admin
         numb_list=1 - Logout in User/Cowner"""
        self.methods.click_element(self.locators.DROPDOWN, numb_list)

    def click_login(self):
        self.click_dropdown(0)

