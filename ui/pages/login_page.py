from selenium.common import NoSuchElementException

from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginLocators



class LoginPage(BasePage):
    def login(self, username, password):
        self.browser.find_element(*LoginLocators.LOGIN).send_keys(username)
        self.browser.find_element(*LoginLocators.PASS).send_keys(password)
        self.browser.find_element(*LoginLocators.BUTTON).click()