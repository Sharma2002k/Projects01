from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    COMPLETE = (By.CLASS_NAME, "complete-header")

    def enter_customer_details(self, first, last, zip_code):
        self.enter_text(self.FIRST_NAME, first)
        self.enter_text(self.LAST_NAME, last)
        self.enter_text(self.POSTAL_CODE, zip_code)

    def continue_checkout(self):
        self.click(self.CONTINUE)

    def finish_order(self):
        self.click(self.FINISH)

    def get_success_message(self):
        return self.get_text(self.COMPLETE)