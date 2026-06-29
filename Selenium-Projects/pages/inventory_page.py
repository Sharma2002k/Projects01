from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")

    def get_page_title(self):
        return self.get_text(self.TITLE)

    def add_backpack(self):
        self.click(self.BACKPACK)

    def add_bike_light(self):
        self.click(self.BIKE_LIGHT)

    def add_bolt_tshirt(self):
        self.click(self.BOLT_TSHIRT)

    def open_cart(self):
        self.click(self.CART)