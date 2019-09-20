import os
import unittest
from version_1.Pages.Login_Page.LoginPageLocators import LoginPageLocators as LoginLocators
from version_1.Objects.Navigation_Bar_Locators import NavigationBarLocators as NavBarLocators
from version_1.Pages.Login_Page.LoginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait


class TestLoginPage(unittest.TestCase):
    LOGIN = os.getenv('PHARMA_PHARMLOGIN')
    PASSWORD = os.getenv('PHARMA_PHARMPASSWORD')

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://pharmacy-test-preprod.newmedicine.com.ua")
        self.driver.maximize_window()

    def test_01_load_page(self):
        driver = self.driver
        assert "Поліклініка без черг" in driver.title

    def test_02_1_enter_submit_without_login(self):
        driver = self.driver
        assert "Поліклініка без черг" in driver.title
        LoginPage(driver).click_submit()
        result = WebDriverWait(driver, 10).until(ex_cond.visibility_of_element_located(LoginLocators.ERROR_MESSAGE))
        assert "Введіть ваш номер телефону" in result.text

    def test_03_1_login_ok_click_Submit(self):
        driver = self.driver
        assert "Поліклініка без черг" in driver.title
        login = WebDriverWait(driver, 10).until(ex_cond.visibility_of_element_located(LoginLocators.LOGIN_INPUT))
        login.clear()
        login.send_keys(self.LOGIN)
        password = WebDriverWait(driver, 10).until(ex_cond.visibility_of_element_located(LoginLocators.PASSWORD_INPUT))
        password.clear()
        password.send_keys(self.PASSWORD)
        WebDriverWait(driver, 10).until(ex_cond.visibility_of_element_located(LoginLocators.SUBMIT)).click()
        result = WebDriverWait(driver, 10).until(ex_cond.visibility_of_element_located(NavBarLocators.MENU_BLOCK))
        assert "Вийти" in result.text

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()