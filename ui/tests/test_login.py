from ..pages.login_page import LoginPage

base = 'https://www.saucedemo.com/'


def test_user_can_login(browser):
    page = LoginPage(browser, base)
    page.open()
    page.set_login('standard_user')
    page.set_password('secret_sauce')
    page.login_click()
    assert page.browser.get_current_url() != base, 'You are not logged in'
