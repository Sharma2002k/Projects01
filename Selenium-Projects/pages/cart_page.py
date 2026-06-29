from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    REMOVE = (By.ID, "remove-sauce-labs-backpack")

    def checkout(self):
        self.click(self.CHECKOUT)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def remove_product(self):
        self.click(self.REMOVE)