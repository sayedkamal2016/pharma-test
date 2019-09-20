from version_1.Objects.Menu_Bar.Menu_Bar_Locators import MenuBarLocators
from version_1.Objects.BaseObject import BaseObject


class MenuBar(BaseObject):
    def __init__(self, driver):
        self.driver = driver

    def click_exit(self):
        pass

    def menu_block_is_loaded(self):
        return self.element_visible(MenuBarLocators.MENU_BLOCK)
