import pytest

from ui.pages.login_page import LoginPage
from ui.locators.login_locators import LoginLocators

base = 'https://www.saucedemo.com/'


def test_user_can_login(browser):
    page = LoginPage(browser, base)
    page.open()
    page.login('standard_user', 'secret_sauce')
    assert page.browser.current_url != base, 'You are not logged in'


@pytest.mark.parametrize('login, password, error', [('standard_user','wrongpass', "Epic sadface: Username and password do not match any user in this service"),
                                                    ('','secret_sauce', "Epic sadface: Username is required"),
                                                    ('standard_user','', "Epic sadface: Password is required"),
                                                    ('locked_out_user','secret_sauce', 'Epic sadface: Sorry, this user has been locked out.')])
def test_login_invalid_data(browser, login, password, error):
    page = LoginPage(browser, base)
    page.open()
    page.login(login, password)
    assert page.browser.find_element(*LoginLocators.ERROR_MESSAGE).text == error
