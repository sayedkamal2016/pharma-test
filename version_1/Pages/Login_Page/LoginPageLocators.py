from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@class='conf auth wide ng-pristine ng-valid ng-scope']")
    SUBMIT = (By.XPATH, "//button[@class='btn btn-green long btn-inline']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'ui-notification ng-scope error clickable')]")
    LOGIN_INPUT = (By.NAME, "EQ_login_auth")
    PASSWORD_INPUT = (By.NAME, "EQ_password_auth")
    FORGET_PASSWORD_LINK = (By.XPATH, "//div[contains(@ng-click,'ctl.ForgetPass()')]")
    FORGET_PASSWORD_FORM = (By.XPATH, "//form[contains(@ng-submit,'ctl.ForgetPassSubmit()')]")
    PHONE_INPUT_FORGET_PASSWORD = (By.XPATH, "//input[contains(@placeholder,'Введіть ваш телефон')]")
