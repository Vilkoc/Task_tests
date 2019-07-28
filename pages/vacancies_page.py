ALL_VACANCIES_LINK_TEXT = 'RabotyNet'
VIEW_DETAILS_BUTTON_CSS_SELECTOR = 'a[href="/viewVacancy/10"]'


class VacanciesPage:

    def __init__(self, driver):
        self.driver = driver

        self.allVacancies_linkText = ALL_VACANCIES_LINK_TEXT
        self.viewDetails_button_cssSelector = VIEW_DETAILS_BUTTON_CSS_SELECTOR

    def go_to_allVacancies(self):
        self.driver.find_element_by_link_text(self.allVacancies_linkText).click()
        # WebDriverWait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/app-root/rabotynet/html/body/div/div[2]/div[1]/div')))

    def click_viewDetails_button(self):
        self.driver.find_element_by_css_selector(self.viewDetails_button_cssSelector).click()
