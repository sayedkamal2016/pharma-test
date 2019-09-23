from selenium.webdriver.common.by import By


class LoginPageLocators:
    def __init__(self):
        pass

    LOGIN_FORM = (By.XPATH, "//form[@class='conf auth wide ng-pristine ng-valid ng-scope']")
    SUBMIT = (By.XPATH, "//button[@class='btn btn-green long btn-inline']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'ui-notification ng-scope error clickable')]")
    LOGIN_INPUT = (By.NAME, "EQ_login_auth")
    PASSWORD_INPUT = (By.NAME, "EQ_password_auth")
    LINK_FORGET_PASSWORD = (By.XPATH, "//div[contains(@ng-click,'ctl.ForgetPass()')]")
    FORGET_PASSWORD_FORM = (By.XPATH, "//form[contains(@ng-submit,'ctl.ForgetPassSubmit()')]")
    PHONE_INPUT_FORGET_PASSWORD = (By.XPATH, "//input[contains(@placeholder,'Введіть ваш телефон')]")
    FORGET_PASSWORD_BUTTON_NEXT = (By.XPATH, "//div[@class='btn-ico confirm'][contains(.,'Далі')]")
    FORGET_PASSWORD_BUTTON_BACK = (By.XPATH, "//div[@class='btn-ico short cancel dark'][contains(.,'Назад')]")
