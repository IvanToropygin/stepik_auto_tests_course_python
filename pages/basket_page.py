from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_login_page(self):
        self.should_be_text_basket_is_empty()
        self.should_be_not_row_with_products_in_basket()

    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Cant find 'Ваша корзина пуста' in cart page"

    def should_be_not_row_with_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ROW_PRODUCTS_IN_BASKET), "Row with products is present"
