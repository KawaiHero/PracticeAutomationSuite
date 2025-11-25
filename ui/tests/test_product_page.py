from ui.pages.login_page import LoginPage
from ui.pages.product_page import ProductPage

base = 'https://www.saucedemo.com/'


def test_user_can_see_products_after_login(browser):
    page = LoginPage(browser, base)
    page.open()
    page.login('standard_user', 'secret_sauce')
    assert page.browser.current_url != base, 'You are not logged in'
    prod_page = ProductPage(browser, base)
    products = prod_page.get_products()
    assert len(products) > 0, 'There should products'

def test_user_can_see_products_price(browser):
    page = LoginPage(browser, base)
    page.open()
    page.login('standard_user', 'secret_sauce')
    assert page.browser.current_url != base, 'You are not logged in'
    prod_page = ProductPage(browser, base)
    products = prod_page.get_product_price(2)
    assert products.startswith("$")

def test_add_to_cart_from_product_page(browser):
    page = LoginPage(browser, base)
    page.open()
    page.login('standard_user', 'secret_sauce')
    assert page.browser.current_url != base, 'You are not logged in'
    prod_page = ProductPage(browser, base)
    prod_page.add_to_cart_from_item_list(3).click()
    prod_page.add_to_cart_from_item_list(4).click()
    prod_page.go_to_shopping_cart()
    cart_products = prod_page.get_products()
    assert len(cart_products) > 0, 'There should products'

