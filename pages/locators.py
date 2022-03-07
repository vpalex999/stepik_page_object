from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success .alertinner")
    MESSAGES = (By.CSS_SELECTOR, "#messages")
    FIRST_SUCCES_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child .alertinner")
    PRICE_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")