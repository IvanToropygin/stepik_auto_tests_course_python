from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_login_page_title_exist_login(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url

def test_login_page_exist_enter_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_login_page_exist_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()