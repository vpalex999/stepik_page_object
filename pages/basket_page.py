from .base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "The basket has some products"

    def should_be_message_empty(self):
        message_empty = self.browser.find_element(
            *BasketPageLocators.MESSAGE).text
        assert message_empty == "Your basket is empty. Continue shopping", "The basket has not message empty"

    def should_be_empty(self):
        self.should_not_be_products()
        self.should_be_message_empty()
