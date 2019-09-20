from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element_click(self, locator):
        return WebDriverWait(self.driver, 10).until(ex_cond.element_to_be_clickable(locator)).click()

    def element_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(ex_cond.visibility_of_element_located(locator))

    def set_text_in_input(self, locator, text):
        inp = WebDriverWait(self.driver, 10).until(ex_cond.element_to_be_clickable(locator))
        inp.clear()
        return inp.send_keys(text)