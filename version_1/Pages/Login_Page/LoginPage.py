from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage
from Pages.Login_Page.LoginPageLocators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_submit(self):
        return self.element_click(LoginPageLocators.SUBMIT)

    def take_error_message(self):
        return self.element_visible(LoginPageLocators.ERROR_MESSAGE)

    def set_login(self, login):
        return self.send_in_input(LoginPageLocators.LOGIN_INPUT, login)

    def set_password(self, password):
        return self.send_in_input(LoginPageLocators.PASSWORD_INPUT, password)

    def press_enter(self):
        return self.send_in_input(LoginPageLocators.PASSWORD_INPUT, Keys.ENTER)

    def press_forget_password(self):
        return self.element_click(LoginPageLocators.LINK_FORGET_PASSWORD)

    def forget_pass_input(self):
        return self.element_visible(LoginPageLocators.PHONE_INPUT_FORGET_PASSWORD)

    def click_back_in_forget_pass(self):
        return self.element_click(LoginPageLocators.FORGET_PASSWORD_BUTTON_BACK)

    def message_click(self):
        return self.element_click(LoginPageLocators.ERROR_MESSAGE)

    def clear_login_input(self):
        self.send_in_input(LoginPageLocators.LOGIN_INPUT, Keys.CONTROL + "a")
        self.send_in_input(LoginPageLocators.LOGIN_INPUT, Keys.DELETE)
