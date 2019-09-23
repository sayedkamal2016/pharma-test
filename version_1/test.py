import os
import unittest
from version_1.Objects.Menu_Bar.MenuBar import MenuBar
from version_1.Pages.Login_Page.LoginPage import LoginPage
from selenium import webdriver


class TestLoginPage(unittest.TestCase):
    LOGIN = os.getenv('PHARMA_PHARMLOGIN')
    PASSWORD = os.getenv('PHARMA_PHARMPASSWORD')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://pharmacy-test-preprod.newmedicine.com.ua")
        self.driver.maximize_window()

    def test_01_load_page(self):
        driver = self.driver
        assert "Поліклініка без черг" in driver.title
        print(driver.title)

    def test_02_1_enter_submit_without_login(self):
        driver = self.driver
        LoginPage(driver).click_submit()
        result = LoginPage(driver).take_error_message()
        assert "Введіть ваш номер телефону" in result.text

    def test_02_2_enter_without_password(self):
        driver = self.driver
        LoginPage(driver).set_login(self.LOGIN)
        LoginPage(driver).press_enter()
        result = LoginPage(driver).take_error_message()
        assert "Введіть ваш пароль" in result.text

    def test_02_3_lost_password(self):
        driver = self.driver
        LoginPage(driver).set_login("0123456789")
        LoginPage(driver).press_forget_password()
        result = LoginPage(driver).forget_pass_input().get_attribute("value")
        assert "0123456789" in result
        LoginPage(driver).click_back_in_forget_pass()
        LoginPage(driver).click_submit()
        result = LoginPage(driver).take_error_message()
        assert "Введіть ваш пароль" in result.text


    def test_03_1_login_ok_click_Submit(self):
        driver = self.driver
        LoginPage(driver).set_login(self.LOGIN)
        LoginPage(driver).set_password(self.PASSWORD)
        LoginPage(driver).click_submit()
        result = MenuBar(driver).menu_block_is_loaded()
        assert "Вийти" in result.text

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
