from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MenuPage(BasePage):

    MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")
    RESET_APP = (By.ID, "reset_sidebar_link")
    ABOUT = (By.ID, "about_sidebar_link")

    def open_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGOUT)
        )

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT)
        ).click()

        # Wait until redirected to login page
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/")
        )

    def reset_app(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.RESET_APP)
        ).click()

    def open_about(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ABOUT)
        ).click()