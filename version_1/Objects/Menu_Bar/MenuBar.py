from version_1.Objects.Menu_Bar.Menu_Bar_Locators import MenuBarLocators
from version_1.Objects.BaseObject import BaseObject


class MenuBar(BaseObject):
    def __init__(self, driver):
        self.driver = driver

    def menu_block_is_loaded(self):
        return self.element_visible(MenuBarLocators.MENU_BLOCK)

    def click_exit(self):
        return self.element_click(MenuBarLocators.EXIT)

    def click_dispense_report(self):
        return  self.element_click(MenuBarLocators.SEARCH_DISPENSES)

    def click_messages(self):
        return self.element_click(MenuBarLocators.MESSAGES)

    def click_settings(self):
        return  self.element_click(MenuBarLocators.SETTINGS)

    def click_search_code(self):
        return self.element_click(MenuBarLocators.SEARCH_CODE)
