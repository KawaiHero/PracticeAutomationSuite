from selenium.webdriver.common.by import By

class ProductLocators:
    ITEM_LIST = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    ADD_TO_CART_FROM_ITEM_LIST = (By.XPATH, '//button[contains(text(),"Add to cart")]')
    ADD_TO_CART_FROM_ITEM_PAGE = (By.CSS_SELECTOR, '[data-test="add-to-cart"]')
    GO_TO_CART = By.CSS_SELECTOR, '[data-test="shopping-cart-link"]'