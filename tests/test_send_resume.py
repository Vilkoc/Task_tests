from conftest import app


def test_send_resume(app):
    app.header.select_option('Log in')
    app.sign_in_page.login('USER')
    app.header.go_to_allVacancies()
    app.vacancies_page.click_viewDetails_button()
    app.view_vacancy_page.click_sendResume_button()
    app.preview_resume_page.click_sendEmail_button()
    msg = app.preview_resume_page.confirmation_message()
    assert msg == "Mail has been sent!"
