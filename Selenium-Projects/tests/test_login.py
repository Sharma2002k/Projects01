import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

BASE_URL = "https://www.saucedemo.com/"


class TestLogin:

    # 1. Valid Login
    def test_valid_login(self, driver):
        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)

        assert inventory.get_page_title() == "Products"

    # 2. Invalid Login
    @pytest.mark.parametrize(
        "username,password",
        [
            ("locked_out_user", "secret_sauce"),
            ("standard_user", "wrong_password"),
            ("", "")
        ]
    )
    def test_invalid_login(self, driver, username, password):

        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login(username, password)

        assert login.get_error_message() != ""

    # 3. Locked Out User
    def test_locked_out_user(self, driver):

        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login("locked_out_user", "secret_sauce")

        assert "locked out" in login.get_error_message().lower()

    # 4. Empty Username
    def test_empty_username(self, driver):

        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login("", "secret_sauce")

        assert login.get_error_message() != ""

    # 5. Empty Password
    def test_empty_password(self, driver):

        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login("standard_user", "")

        assert login.get_error_message() != ""

    # 6. Empty Username and Password
    def test_empty_credentials(self, driver):

        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login("", "")

        assert login.get_error_message() != ""

    # 7. Invalid Username
    def test_invalid_username(self, driver):

        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login("khushi", "secret_sauce")

        assert login.get_error_message() != ""

    # 8. Invalid Password
    def test_invalid_password(self, driver):

        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login("standard_user", "abc123")

        assert login.get_error_message() != ""

    # 9. SQL Injection Attempt
    def test_sql_injection_login(self, driver):

        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login("' OR '1'='1", "' OR '1'='1")

        assert login.get_error_message() != ""

    # 10. Special Characters Login
    def test_special_character_login(self, driver):

        driver.get(BASE_URL)

        login = LoginPage(driver)
        login.login("@#$%^&*", "!@#$%^")

        assert login.get_error_message() != ""