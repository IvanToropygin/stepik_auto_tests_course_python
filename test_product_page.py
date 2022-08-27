from pages.product_page import ProductPage


def test_click_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    price_on_product_page = page.get_price_on_product_page()
    name_on_product_page = page.get_product_name_on_product_page()
    page.click_on_add_to_cart_btn()
    page.solve_quiz_and_get_code()
    amount_cart_in_success_message = page.get_amount_cart_in_success_message()
    page.should_be_amount_in_cart(price_on_product_page, amount_cart_in_success_message)
    name_of_product_in_success_message = page.get_product_name_in_success_message()
    page.should_be_name_of_product_in_success_message(name_on_product_page, name_of_product_in_success_message)

def test_click_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    price_on_product_page = page.get_price_on_product_page()
    name_on_product_page = page.get_product_name_on_product_page()
    page.click_on_add_to_cart_btn()
    page.solve_quiz_and_get_code()
    amount_cart_in_success_message = page.get_amount_cart_in_success_message()
    page.should_be_amount_in_cart(price_on_product_page, amount_cart_in_success_message)
    name_of_product_in_success_message = page.get_product_name_in_success_message()
    page.should_be_name_of_product_in_success_message(name_on_product_page, name_of_product_in_success_message)
