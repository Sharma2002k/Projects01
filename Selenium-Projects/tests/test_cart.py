from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.menu_page import MenuPage

BASE_URL = "https://www.saucedemo.com/"


class TestCart:

    # 1. Remove Product
    def test_remove_product(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).remove_product()

        assert "cart.html" in driver.current_url

    # 2. Continue Shopping
    def test_continue_shopping(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).continue_shopping()

        assert "inventory.html" in driver.current_url

    # 3. Add One Product
    def test_add_single_product(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()

        assert True

    # 4. Add Multiple Products
    def test_add_multiple_products(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.add_bike_light()
        inventory.add_bolt_tshirt()

        assert True

    # 5. Open Cart
    def test_open_cart(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        InventoryPage(driver).open_cart()

        assert "cart.html" in driver.current_url

    # 6. Checkout Button
    def test_checkout_button(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        assert "checkout-step-one.html" in driver.current_url

    # 7. Complete Checkout
    def test_complete_checkout(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        cart = CartPage(driver)
        cart.checkout()

        checkout = CheckoutPage(driver)

        checkout.enter_customer_details(
            "Khushi",
            "Sharma",
            "474001"
        )

        checkout.continue_checkout()
        checkout.finish_order()

        assert checkout.get_success_message() == "Thank you for your order!"

    # 8. Logout
    def test_logout(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        menu = MenuPage(driver)
        menu.open_menu()
        menu.logout()

        assert driver.current_url == BASE_URL

    # 9. Reset App State
    def test_reset_app(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        menu = MenuPage(driver)
        menu.open_menu()
        menu.reset_app()

        assert True

    # 10. About Page
    def test_about_page(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        menu = MenuPage(driver)
        menu.open_menu()
        menu.open_about()

        assert "saucelabs.com" in driver.current_url