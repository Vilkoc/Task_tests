import pytest
from init import resource_setup

import allure

# @pytest.mark.usefixtures('resource_setup1')
@allure.story('Login test')
@pytest.mark.parametrize('user, password, expected', [
    ('admin@gmail.com', 'admin', 'Сompanies'),
    ('user@gmail.com', 'user', 'Create company1'),
    ('cowner@gmail.com', 'cowner', 'My companies')
    ])
def test_login_logout(resource_setup, user, password, expected):
    """ Testcase for user login.
        Try to login for each user"""
    page = resource_setup

    page.header.click_icon()
    page.header.click_log_in()

    page.sign_in_page.enter_sign_in_email(user)
    page.sign_in_page.enter_sign_in_password(password)
    page.sign_in_page.click_sign_in()

    with allure.step('Check if user logined'):
        assert page.header.is_logined()
        page.header.click_icon()

    with allure.step('Check if user authorized'):
        assert page.header.get_text_of_first_link() == expected

    page.header.click_icon()
    page.header.click_log_out()
