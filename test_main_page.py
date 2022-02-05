
def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    browser.get(link)
    go_to_login_page(browser)

def test_add_to_cart(browser):
    page = ProductPage(url="", browser)
    page.open()
    page.should_be_add_to_catr_button()
    page.app_product_to_cart()
    page.should_be_success_message()