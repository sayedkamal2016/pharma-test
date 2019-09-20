from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element_click(self, locator):
        return WebDriverWait(self.driver, 10).until(ex_cond.element_to_be_clickable(locator)).click()
