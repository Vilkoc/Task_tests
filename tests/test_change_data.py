from conftest import app


def test_change_data(app):
    app.header.select_option('Log in')
    app.sign_in_page.login('USER')
    app.header.go_to_allVacancies()
    app.vacancies_page.click_viewDetails_button()
    app.view_vacancy_page.click_sendResume_button()
    app.preview_resume_page.click_change_button()
    app.edit_resume_page.change_positionField('Junior Developer')
    app.edit_resume_page.click_previewPDF_button()
    app.preview_resume_page.click_change_button()
    text = app.edit_resume_page.confirmation_changes()
    assert text == 'Junior Developer'
