from ui.pages.base_page import BasePage
from ui.locators.product_locators import ProductLocators

class ProductPage(BasePage):
    def get_products(self):
        return self.browser.find_elements(*ProductLocators.ITEM_LIST)

    def get_product_price(self, index=0):
        return self.browser.find_elements(*ProductLocators.PRODUCT_PRICE)[index].text

    def add_to_cart_from_item_list(self, index=0):
        return self.browser.find_elements(*ProductLocators.ADD_TO_CART_FROM_ITEM_LIST)[index]

    def go_to_shopping_cart(self):
        return self.browser.find_element(*ProductLocators.GO_TO_CART).click()