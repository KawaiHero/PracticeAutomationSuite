from selenium.common import NoSuchElementException

from base_page import BasePage
from ..locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def set_login(self, username):
        try:
            login = self.is_element_present(*LoginLocators.LOGIN)
            login.clear()
            login.send_keys(username)
        except NoSuchElementException:
            return False
        return True

    def set_password(self, password):
        try:
            login = self.is_element_present(*LoginLocators.PASS)
            login.clear()
            login.send_keys(password)
        except NoSuchElementException:
            return False
        return True

    def login_click(self):
        button = self.browser.find_element(*LoginLocators.BUTTON)
        button.click()