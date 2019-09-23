from selenium.webdriver.common.by import By


class MenuBarLocators:
    def __init__(self):
        pass

    MENU_BLOCK = (By.XPATH, "//div[contains(@class,'navbar ng-scope')]")
    SEARCH_CODE = (By.XPATH, "//a[@ui-sref='subNavBar.reinbursation.code']")
    SEARCH_DISPENSES = (By.XPATH, "//a[@ui-sref='subNavBar.reinbursation.dispenses']")
    MESSAGES = (By.XPATH, "//a[@ui-sref='system.messages']")
    SETTINGS = (By.XPATH, "//a[@ui-sref='system.setups']")
    EXIT = (By.XPATH, "//a[@ng-show='ctl.allowByRole(ctl.closeButton)']")
