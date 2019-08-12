from init import SeleniumTestBase
from data_tests.cowner_data import CownerData


class TestCreateVacancy(SeleniumTestBase):

    def test_create_vacancy(self):

        self.header.select_option(CownerData.OPTION)
        self.sign_in_page.login(CownerData.PERSON)

        self.header.click_my_companies()
        self.my_companies_page.click_view_details()
        self.view_company_page.click_create_vacancy()
        self.create_vacancy_page.enter_vacancy_data(CownerData.VACANCY_DATA)
        self.create_vacancy_page.choose_employment()
        self.create_vacancy_page.choose_currency()
        self.create_vacancy_page.click_add_requirement()
        self.create_vacancy_page.enter_requirements(CownerData.REQUIREMENTS)
        self.create_vacancy_page.click_vacancy_create()
        self.view_company_page.view_vacancy_details(CownerData.VACANCY_NAME)
        all_vacancy_data = self.create_vacancy_page.read_vacancy_data()

        num_of_vac_data = 0
        for vac_data in CownerData.VACANCY_DATA:
            assert vac_data == all_vacancy_data[num_of_vac_data]
            num_of_vac_data += 1
