from version_1.Pages.BasePage import BasePage
from version_1.Pages.Login_Page.LoginPageLocators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_submit(self):
        self.element_click(LoginPageLocators.SUBMIT)
