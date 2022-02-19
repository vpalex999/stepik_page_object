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

    def should_be_message_box(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGES), f"The messages are not present"

    def should_be_message_to_add_product(self, product_name: str) -> None:
        self.should_be_message_box()

        alerts = self.browser.find_elements(*ProductPageLocators.ALERT_SUCCESS)
        alerts_success_text = [element.text.strip() for element in alerts]

        assert any([text.find(product_name) for text in alerts_success_text]), \
            f"Not found product name '{product_name}' in alerts success: {alerts_success_text}"

    def should_be_price_basket_equal_to_price_product(self, price):
        price_basket_message = self.browser.find_element(
            *ProductPageLocators.PRICE_BASKET_MESSAGE).text

        assert price_basket_message.find(price), \
            f"The basket total '{price_basket_message}' price is not equal price of added product '{price}'"
