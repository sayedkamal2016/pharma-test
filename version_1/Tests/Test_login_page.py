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
        self.driver.maximize_window()
        self.driver.get("https://pharmacy-test-preprod.newmedicine.com.ua")

    def test_01_load_page(self):
        driver = self.driver
        self.assertEqual(driver.title, "Поліклініка без черг", "Page title is wrong:")

    def test_02_1_enter_submit_without_login(self):
        driver = self.driver
        LoginPage(driver).click_submit()
        result = LoginPage(driver).take_error_message()
        self.assertEqual(result.text, "Введіть ваш номер телефону", False)

    def test_02_2_enter_without_password(self):
        driver = self.driver
        LoginPage(driver).set_login(self.LOGIN)
        LoginPage(driver).press_enter()
        result = LoginPage(driver).take_error_message()
        self.assertEqual(result.text, "Введіть ваш пароль", False)

    def test_02_3_lost_password_and_return(self):
        driver = self.driver
        LoginPage(driver).set_login("0123456789")
        LoginPage(driver).press_forget_password()
        phone_number = LoginPage(driver).forget_pass_input().get_attribute("value")
        self.assertEqual(phone_number, "0123456789", False)
        LoginPage(driver).click_back_in_forget_pass()
        LoginPage(driver).click_submit()
        result = LoginPage(driver).take_error_message()
        self.assertEqual(result.text, "Введіть ваш пароль", False)

    def test_03_1_login_ok_click_Submit(self):
        driver = self.driver
        LoginPage(driver).set_login(self.LOGIN)
        LoginPage(driver).set_password(self.PASSWORD)
        LoginPage(driver).click_submit()
        result = MenuBar(driver).menu_block_is_loaded()
        self.assertEqual(result.text, "Вийти", False)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
