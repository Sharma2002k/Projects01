from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

BASE_URL = "https://www.saucedemo.com/"


class TestInventory:

    # 1. Add Single Product
    def test_add_single_product(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        WebDriverWait(driver, 10).until(
            EC.url_contains("cart.html")
        )

        assert "cart.html" in driver.current_url

    # 2. Add Multiple Products
    def test_add_multiple_products(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)

        inventory.add_backpack()
        inventory.add_bike_light()
        inventory.add_bolt_tshirt()

        inventory.open_cart()

        WebDriverWait(driver, 10).until(
            EC.url_contains("cart.html")
        )

        assert "cart.html" in driver.current_url

    # 3. Inventory Page Title
    def test_inventory_page_title(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)

        assert inventory.get_page_title() == "Products"

    # 4. Inventory URL
    def test_inventory_url(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        assert "inventory.html" in driver.current_url

    # 5. Add Backpack
    def test_add_backpack(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        InventoryPage(driver).add_backpack()

        assert True

    # 6. Add Bike Light
    def test_add_bike_light(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        InventoryPage(driver).add_bike_light()

        assert True

    # 7. Add Bolt T-Shirt
    def test_add_bolt_tshirt(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        InventoryPage(driver).add_bolt_tshirt()

        assert True

    # 8. Add All Products
    def test_add_all_products(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)

        inventory.add_backpack()
        inventory.add_bike_light()
        inventory.add_bolt_tshirt()

        assert "inventory.html" in driver.current_url

    # 9. Open Cart
    def test_open_cart(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)

        inventory.open_cart()

        WebDriverWait(driver, 10).until(
            EC.url_contains("cart.html")
        )

        assert "cart.html" in driver.current_url

    # 10. Login to Inventory Page
    def test_login_inventory_page(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        assert "inventory.html" in driver.current_url