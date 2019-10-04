import os
import unittest
from typing import Any, Union

from selenium import webdriver

from Objects.Menu_Bar.MenuBar import MenuBar
from Pages.Login_Page.LoginPage import LoginPage


class TestLoginPage(unittest.TestCase):
    LOGIN = os.getenv('PHARMA_LOGIN')
    PASSWORD = os.getenv('PHARMA_PASSWORD')
    URL = ''

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        #options.add_argument('disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.get(self.URL)

    # def test_01_load_page(self):
    #     driver = self.driver
    #     self.assertEqual("Поліклініка без черг", driver.title, "Page title is wrong:")
    #
    # def test_02_1_enter_submit_without_login(self):
    #     driver = self.driver
    #     LoginPage(driver).click_submit()
    #     result = LoginPage(driver).take_error_message()
    #     self.assertEqual("Введіть ваш номер телефону", result.text, "Has no popup 'Введіть ваш номер телефону'")
    #
    # def test_02_2_enter_without_password(self):
    #     driver = self.driver
    #     LoginPage(driver).set_login(self.LOGIN)
    #     LoginPage(driver).press_enter()
    #     result = LoginPage(driver).take_error_message()
    #     self.assertEqual("Введіть ваш пароль", result.text, "Has no popup 'Введіть ваш пароль'")
    #
    # def test_02_3_lost_password_and_return(self):
    #     driver = self.driver
    #     LoginPage(driver).set_login("0123456789")
    #     LoginPage(driver).press_forget_password()
    #     phone_number = LoginPage(driver).forget_pass_input().get_attribute("value")
    #     self.assertEqual(phone_number, "0123456789", "Has no phone in input")
    #     LoginPage(driver).click_back_in_forget_pass()
    #     LoginPage(driver).click_submit()
    #     result = LoginPage(driver).take_error_message()
    #     self.assertEqual("Введіть ваш пароль", result.text, "Has no popup 'Введіть ваш пароль'")
    #
    # def test_03_1_login_ok_click_Submit(self):
    #     driver = self.driver
    #     LoginPage(driver).set_login(self.LOGIN)
    #     LoginPage(driver).set_password(self.PASSWORD)
    #     LoginPage(driver).click_submit()
    #     result = MenuBar(driver).menu_block_is_loaded()
    #     self.assertIn("Вийти", result.text, "Has no menu bar")

    def test_pharmacy_site_is_start(self):
        print()
        driver = self.driver
        print("check title")
        self.assertEqual("Поліклініка без черг", driver.title, "Page title is wrong:")
        LoginPage(driver).click_submit()
        result = LoginPage(driver).take_error_message()
        print("check error login message")
        self.assertEqual("Введіть ваш номер телефону", result.text, "Has no popup 'Введіть ваш номер телефону'")
        LoginPage(driver).message_click()
        LoginPage(driver).set_login(self.LOGIN)
        LoginPage(driver).press_enter()
        result2 = LoginPage(driver).take_error_message()
        print("check error password message")
        self.assertEqual("Введіть ваш пароль", result2.text, "Has no popup 'Введіть ваш пароль'")
        LoginPage(driver).message_click()
        LoginPage(driver).clear_login_input()
        LoginPage(driver).set_login("0123456789")
        LoginPage(driver).press_forget_password()
        phone_number = LoginPage(driver).forget_pass_input().get_attribute("value")
        print("check save login in forget page")
        self.assertEqual(phone_number, "0123456789", "Has no phone in input")
        LoginPage(driver).click_back_in_forget_pass()
        LoginPage(driver).click_submit()
        result3 = LoginPage(driver).take_error_message()
        self.assertEqual("Введіть ваш пароль", result3.text, "Has no popup 'Введіть ваш пароль'")
        LoginPage(driver).message_click()
        LoginPage(driver).clear_login_input()
        print("check successful login")
        LoginPage(driver).set_login(self.LOGIN)
        LoginPage(driver).set_password(self.PASSWORD)
        LoginPage(driver).click_submit()
        result4 = MenuBar(driver).menu_block_is_loaded()
        self.assertIn("Вийти", result4.text, "Has no menu bar")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
