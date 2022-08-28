from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    GO_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-group>a")

class LoginPageLocators():
    ENTER_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    AMOUNT_CART_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages p:nth-child(1)>strong")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@value='Добавить в корзину']")
    PRICE_ON_PRODUCT_PAGE = (By.XPATH, "//p[@class='price_color']")
    NAME_ON_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product_main>h1")
    MESSAGE_PRODUCT_ADD_TO_CART = (By.XPATH, "//article[@class='product_page']//h1")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

class BasketPageLocators():
    BASKET_IS_EMPTY = (By.XPATH, "//*[@class='content']//*[contains(text(),'Ваша корзина пуста')]")
    ROW_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items>.row")
