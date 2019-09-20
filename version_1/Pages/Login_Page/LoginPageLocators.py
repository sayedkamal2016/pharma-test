from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@class='conf auth wide ng-pristine ng-valid ng-scope']")
    SUBMIT = (By.XPATH, "//div[@class='btn-ico confirm'][contains(.,'Увійти')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'ui-notification ng-scope error clickable')]")
    LOGIN_INPUT = (By.NAME, "EQ_login_auth")
    PASSWORD_INPUT = (By.NAME, "EQ_password_auth")
    FORGET_PASSWORD = (By.XPATH, "//div[contains(@ng-click,'ctl.ForgetPass()')]")
