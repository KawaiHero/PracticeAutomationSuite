from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN = (By.CSS_SELECTOR, '[data-test="username"]')
    PASS = (By.CSS_SELECTOR, '[data-test="password"]')
    BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')