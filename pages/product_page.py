from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button_submit = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BTN)
        button_submit.click()

    def get_product_name(self) -> str:
        name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        return name

    def get_product_price(self) -> str:
        price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        return price

    def should_be_add_product(self):

        product_name = self.get_product_name()
        product_price = self.get_product_price()

        self.should_be_message_to_add_product(product_name)
        self.should_be_price_basket_equal_to_price_product(product_price)

    def should_be_message_to_add_product(self, product_name: str) -> None:

        expected_success_added_message = f"{product_name} has been added to your basket."

        success_added_message = self.browser.find_element(
            *ProductPageLocators.FIRST_SUCCES_MESSAGE).text

        assert success_added_message == expected_success_added_message, \
            f"expected success message '{expected_success_added_message}' is not equal actual: '{success_added_message}'"

    def should_be_price_basket_equal_to_price_product(self, price):
        price_basket_message = self.browser.find_element(
            *ProductPageLocators.PRICE_BASKET_MESSAGE).text

        assert price_basket_message.find(price), \
            f"The basket total '{price_basket_message}' price is not equal price of added product '{price}'"
