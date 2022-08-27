from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_go_to_login_page(browser):
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

