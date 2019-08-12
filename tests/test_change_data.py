from init import setup
# from init import page_init


def test_change_data(setup):
    page_init = setup
    page_init.get('header').select_option('Log in')
    page_init.get('sign_in_page').login('USER')
    page_init.get('header').go_to_allVacancies()
    page_init.get('vacancies_page').click_viewDetails_button()
    page_init.get('view_vacancy_page').click_sendResume_button()
    page_init.get('preview_resume_page').click_change_button()
    page_init.get('edit_resume_page').change_positionField('Middle Developer')
    page_init.get('edit_resume_page').click_previewPDF_button()
    page_init.get('preview_resume_page').click_change_button()
    text = page_init.get('edit_resume_page').confirmation_changes()
    assert text == 'Middle Developer'


