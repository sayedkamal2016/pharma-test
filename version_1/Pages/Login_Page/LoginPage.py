from version_1.Pages.BasePage import BasePage
from version_1.Pages.Login_Page.LoginPageLocators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_submit(self):
        self.element_click(LoginPageLocators.SUBMIT)

    def take_error_message(self):
        return self.element_visible(LoginPageLocators.ERROR_MESSAGE)

    def set_login(self, login):
        self.set_text_in_input(LoginPageLocators.LOGIN_INPUT, login)

    def set_password(self, password):
        self.set_text_in_input(LoginPageLocators.PASSWORD_INPUT, password)
