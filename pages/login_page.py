import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Cant find word 'login' in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.ENTER_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_fake_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "!Password"
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD1_INPUT)
        password_input.send_keys(password)
        password_input_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD2_INPUT)
        password_input_confirm.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()

