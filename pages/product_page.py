from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_login_page(self):
        self.click_on_add_to_cart_btn()
        self.get_price_on_product_page()
        self.get_product_name_on_product_page()
        self.get_product_name_in_success_message()
        self.get_amount_cart_in_success_message()
        self.should_be_amount_in_cart()
        self.should_be_name_of_product_in_success_message()


    def click_on_add_to_cart_btn(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def get_price_on_product_page(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_ON_PRODUCT_PAGE).text.split(" ")[0]

    def get_product_name_on_product_page(self):
        return self.browser.find_element(*ProductPageLocators.NAME_ON_PRODUCT_PAGE).text

    def get_product_name_in_success_message(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_CART).text

    def get_amount_cart_in_success_message(self):
        return self.browser.find_element(*ProductPageLocators.AMOUNT_CART_IN_SUCCESS_MESSAGE).text.split(" ")[0]

    def should_be_amount_in_cart(self, expected, actual):
        assert expected == actual, "amount in cart unexpected"

    def should_be_name_of_product_in_success_message(self, expected, actual):
        assert expected == actual, "name of product in success message unexpected"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
              "Success message must disappeared"
