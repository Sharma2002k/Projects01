from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

BASE_URL = "https://www.saucedemo.com/"


class TestCheckout:

    # 1. Complete Checkout
    def test_complete_checkout(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("Khushi", "Sharma", "474001")
        checkout.continue_checkout()
        checkout.finish_order()

        assert checkout.get_success_message() == "Thank you for your order!"

    # 2. Empty First Name
    def test_empty_first_name(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("", "Sharma", "474001")
        checkout.continue_checkout()

        assert "checkout-step-one.html" in driver.current_url

    # 3. Empty Last Name
    def test_empty_last_name(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("Khushi", "", "474001")
        checkout.continue_checkout()

        assert "checkout-step-one.html" in driver.current_url

    # 4. Empty Postal Code
    def test_empty_postal_code(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("Khushi", "Sharma", "")
        checkout.continue_checkout()

        assert "checkout-step-one.html" in driver.current_url

    # 5. Empty All Fields
    def test_empty_all_fields(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("", "", "")
        checkout.continue_checkout()

        assert "checkout-step-one.html" in driver.current_url

    # 6. Numeric First Name
    def test_numeric_first_name(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("12345", "Sharma", "474001")
        checkout.continue_checkout()

        assert "checkout-step-two.html" in driver.current_url

    # 7. Long First Name
    def test_long_first_name(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("A"*100, "Sharma", "474001")
        checkout.continue_checkout()

        assert "checkout-step-two.html" in driver.current_url

    # 8. Special Characters in Name
    def test_special_characters_name(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("@@@@", "####", "474001")
        checkout.continue_checkout()

        assert "checkout-step-two.html" in driver.current_url

    # 9. Invalid Postal Code
    def test_invalid_postal_code(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("Khushi", "Sharma", "ABCDE")
        checkout.continue_checkout()

        assert "checkout-step-two.html" in driver.current_url

    # 10. Checkout with Multiple Products
    def test_checkout_multiple_products(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.add_bike_light()
        inventory.add_bolt_tshirt()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("Khushi", "Sharma", "474001")
        checkout.continue_checkout()
        checkout.finish_order()

        assert checkout.get_success_message() == "Thank you for your order!"

    # 11. Different Customer Details
    def test_different_customer(self, driver):
        driver.get(BASE_URL)

        LoginPage(driver).login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.open_cart()

        CartPage(driver).checkout()

        checkout = CheckoutPage(driver)
        checkout.enter_customer_details("John", "Doe", "10001")
        checkout.continue_checkout()
        checkout.finish_order()

        assert checkout.get_success_message() == "Thank you for your order!"