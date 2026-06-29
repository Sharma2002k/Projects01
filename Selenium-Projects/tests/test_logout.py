from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


BASE_URL = "https://www.saucedemo.com/"


class TestLogout:


    def login(self,driver):

        driver.get(BASE_URL)

        LoginPage(driver).login(
            "standard_user",
            "secret_sauce"
        )

        WebDriverWait(driver,10).until(
            EC.url_contains("inventory")
        )



    # Test Case 1
    def test_logout_success(self,driver):

        self.login(driver)

        logout = LogoutPage(driver)

        logout.click_menu()
        logout.logout()

        assert driver.current_url == BASE_URL



    # Test Case 2
    def test_login_button_after_logout(self,driver):

        self.login(driver)

        logout = LogoutPage(driver)

        logout.click_menu()
        logout.logout()

        assert logout.verify_login_page()



    # Test Case 3
    def test_username_visible_after_logout(self,driver):

        self.login(driver)

        logout = LogoutPage(driver)

        logout.click_menu()
        logout.logout()

        assert driver.find_element(
            *logout.USERNAME
        ).is_displayed()



    # Test Case 4
    def test_password_visible_after_logout(self,driver):

        self.login(driver)

        logout = LogoutPage(driver)

        logout.click_menu()
        logout.logout()

        assert driver.find_element(
            *logout.PASSWORD
        ).is_displayed()



    # Test Case 5
    def test_relogin_after_logout(self,driver):

        self.login(driver)

        logout = LogoutPage(driver)

        logout.click_menu()
        logout.logout()


        LoginPage(driver).login(
            "standard_user",
            "secret_sauce"
        )


        WebDriverWait(driver,10).until(
            EC.url_contains("inventory")
        )


        assert "inventory" in driver.current_url