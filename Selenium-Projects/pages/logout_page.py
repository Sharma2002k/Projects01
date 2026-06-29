from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LogoutPage(BasePage):

    MENU = (By.ID,"react-burger-menu-btn")
    LOGOUT = (By.ID,"logout_sidebar_link")

    LOGIN_BUTTON = (By.ID,"login-button")
    USERNAME = (By.ID,"user-name")
    PASSWORD = (By.ID,"password")


    def click_menu(self):

        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.MENU)
        ).click()



    def logout(self):

        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.LOGOUT)
        ).click()



    def verify_login_page(self):

        return WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(
                self.LOGIN_BUTTON
            )
        ).is_displayed()