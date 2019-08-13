from conftest import app


def test_send_claim(app):
    app.header.select_option('Log in')
    app.sign_in_page.login('USER')
    app.header.go_to_allVacancies()
    app.vacancies_page.click_viewDetails_button()
    app.view_vacancy_page.click_showCompany_button()
    app.view_company_page.click_claim_button()
    app.view_company_page.choose_option()
    app.view_company_page.fill_out_description_field('description')
    app.view_company_page.click_send_claim_button()

    app.header.select_option('Log out')
    app.header.select_option('Log in')
    app.sign_in_page.login("ADMIN")
    app.companies_page.click_show_claims_button()
    text = app.companies_page.find_description('description')
    assert text == 'description'
