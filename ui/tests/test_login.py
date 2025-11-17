from ui.pages.login_page import LoginPage

base = 'https://www.saucedemo.com/'


def test_user_can_login(browser):
    page = LoginPage(browser, base)
    page.open()
    page.login('standard_user', 'secret_sauce')
    assert page.browser.current_url != base, 'You are not logged in'
