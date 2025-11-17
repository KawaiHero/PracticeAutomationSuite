from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    def wait_visible(self, locator, timeout=15):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator, timeout=15):
        return WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def safe_get_text(self, locator, timeout=10):
        el = self.wait_visible(locator, timeout)
        return el.text.strip()

    def click(self, locator, timeout=15):
        self.wait_clickable(locator, timeout).click()
