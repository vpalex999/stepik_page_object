from .base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button_submit = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BTN)
        button_submit.click()

    def should_be_add_product(self, name: str):
        self.should_be_message_box()
        
        alerts = self.browser.find_elements(*ProductPageLocators.ALERT_SUCCESS)
        alerts_success_text = [element.text.strip() for element in alerts]
        assert any([text.find(name) for text in alerts_success_text]), f"Not found product name '{name}' in alerts success: {alerts_success_text}"

    def should_be_message_box(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGES), f"The messages are not present"