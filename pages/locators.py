from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success .alertinner")
    MESSAGES = (By.CSS_SELECTOR, "#messages")
    PRICE_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")