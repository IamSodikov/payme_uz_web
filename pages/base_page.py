from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def click_element(self, locator):
        WebDriverWait(self.browser, 10).until(
        EC.element_to_be_clickable(locator)
        ).click()


    def is_element_visible(self, locator):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def is_element_clickable(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except:
            return False
    def wait_for_url_contains(self, url_fragment, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            EC.url_contains(url_fragment)
        )

    def get_element_text(self, locator):
        element = self.is_element_visible(locator)
        return element.text